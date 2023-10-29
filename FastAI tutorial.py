#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fastai.vision.all import *


# In[3]:


path = untar_data(URLs.PETS)


# In[4]:


path.ls()


# In[5]:


files = get_image_files(path/"images")
len(files)


# In[6]:


files[0],files[6]


# In[7]:


def label_func(f): return f[0].isupper()


# In[8]:


dls = ImageDataLoaders.from_name_func(path, files, label_func, item_tfms=Resize(224))


# In[9]:


dls.show_batch()


# In[10]:


learn = vision_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(1)


# In[11]:


learn.predict(files[0])


# In[12]:


learn.show_results()


# In[13]:


files[0].name


# In[14]:


pat = r'^(.*)_\d+.jpg'


# In[15]:


dls = ImageDataLoaders.from_name_re(path, files, pat, item_tfms=Resize(224))


# In[16]:


dls.show_batch()


# In[17]:


dls = ImageDataLoaders.from_name_re(path, files, pat, item_tfms=Resize(460),
                                    batch_tfms=aug_transforms(size=224))


# In[18]:


dls.show_batch()


# In[19]:


learn = vision_learner(dls, resnet34, metrics=error_rate)


# In[20]:


learn.lr_find()


# In[ ]:


learn.fine_tune(2, 3e-3)


# In[22]:


learn.show_results()


# In[23]:


interp = Interpretation.from_learner(learn)


# In[24]:


interp.plot_top_losses(9, figsize=(15,10))


# In[25]:


pets = DataBlock(blocks=(ImageBlock, CategoryBlock), 
                 get_items=get_image_files, 
                 splitter=RandomSplitter(),
                 get_y=using_attr(RegexLabeller(r'(.+)_\d+.jpg$'), 'name'),
                 item_tfms=Resize(460),
                 batch_tfms=aug_transforms(size=224))


# In[26]:


dls = pets.dataloaders(untar_data(URLs.PETS)/"images")


# In[27]:


dls.show_batch(max_n=9)


# In[28]:


path = untar_data(URLs.PASCAL_2007)
path.ls()


# In[29]:


df = pd.read_csv(path/'train.csv')
df.head()


# In[30]:


dls = ImageDataLoaders.from_df(df, path, folder='train', valid_col='is_valid', label_delim=' ',
                               item_tfms=Resize(460), batch_tfms=aug_transforms(size=224))


# In[31]:


dls.show_batch()


# In[32]:


f1_macro = F1ScoreMulti(thresh=0.5, average='macro')
f1_macro.name = 'F1(macro)'
f1_samples = F1ScoreMulti(thresh=0.5, average='samples')
f1_samples.name = 'F1(samples)'
learn = vision_learner(dls, resnet50, metrics=[partial(accuracy_multi, thresh=0.5), f1_macro, f1_samples])


# In[33]:


learn.lr_find()


# In[34]:


learn.fine_tune(2, 3e-2)


# In[35]:


learn.show_results()


# In[36]:


learn.predict(path/'train/000005.jpg')


# In[37]:


interp = Interpretation.from_learner(learn)
interp.plot_top_losses(9)


# In[38]:


df.head()


# In[39]:


pascal = DataBlock(blocks=(ImageBlock, MultiCategoryBlock),
                   splitter=ColSplitter('is_valid'),
                   get_x=ColReader('fname', pref=str(path/'train') + os.path.sep),
                   get_y=ColReader('labels', label_delim=' '),
                   item_tfms = Resize(460),
                   batch_tfms=aug_transforms(size=224))


# In[40]:


dls = pascal.dataloaders(df)


# In[41]:


dls.show_batch(max_n=9)


# In[42]:


path = untar_data(URLs.CAMVID_TINY)
path.ls()


# In[43]:


codes = np.loadtxt(path/'codes.txt', dtype=str)
codes


# In[44]:


fnames = get_image_files(path/"images")
fnames[0]


# In[45]:


(path/"labels").ls()[0]


# In[46]:


def label_func(fn): return path/"labels"/f"{fn.stem}_P{fn.suffix}"


# In[47]:


dls = SegmentationDataLoaders.from_label_func(
    path, bs=8, fnames = fnames, label_func = label_func, codes = codes
)


# In[48]:


dls.show_batch(max_n=6)


# In[49]:


learn = unet_learner(dls, resnet34)
learn.fine_tune(6)


# In[50]:


learn.show_results(max_n=6, figsize=(7,8))


# In[51]:


interp = SegmentationInterpretation.from_learner(learn)
interp.plot_top_losses(k=3)


# In[52]:


camvid = DataBlock(blocks=(ImageBlock, MaskBlock(codes)),
                   get_items = get_image_files,
                   get_y = label_func,
                   splitter=RandomSplitter(),
                   batch_tfms=aug_transforms(size=(120,160)))


# In[53]:


dls = camvid.dataloaders(path/"images", path=path, bs=8)


# In[54]:


dls.show_batch(max_n=6)


# In[55]:


path = untar_data(URLs.BIWI_HEAD_POSE)


# In[56]:


path.ls()


# In[57]:


(path/'01').ls()


# In[58]:


img_files = get_image_files(path)
def img2pose(x): return Path(f'{str(x)[:-7]}pose.txt')
img2pose(img_files[0])


# In[59]:


im = PILImage.create(img_files[0])
im.shape


# In[60]:


im.to_thumb(160)


# In[61]:


cal = np.genfromtxt(path/'01'/'rgb.cal', skip_footer=6)
def get_ctr(f):
    ctr = np.genfromtxt(img2pose(f), skip_header=3)
    c1 = ctr[0] * cal[0][0]/ctr[2] + cal[0][2]
    c2 = ctr[1] * cal[1][1]/ctr[2] + cal[1][2]
    return tensor([c1,c2])


# In[62]:


get_ctr(img_files[0])


# In[63]:


biwi = DataBlock(
    blocks=(ImageBlock, PointBlock),
    get_items=get_image_files,
    get_y=get_ctr,
    splitter=FuncSplitter(lambda o: o.parent.name=='13'),
    batch_tfms=[*aug_transforms(size=(240,320)), 
                Normalize.from_stats(*imagenet_stats)]
)


# In[64]:


dls = biwi.dataloaders(path)
dls.show_batch(max_n=9, figsize=(8,6))


# In[65]:


learn = vision_learner(dls, resnet18, y_range=(-1,1))


# In[66]:


learn.lr_find()


# In[67]:


learn.fine_tune(1, 5e-3)


# In[68]:


math.sqrt(0.0001)


# In[69]:


learn.show_results()


# In[ ]:





# In[ ]:





# In[ ]:




