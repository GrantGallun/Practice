from fastai.vision.all import*
from bs4 import BeautifulSoup

page_to_scrape = requests.get("https://www.heb.com/product-detail/h-e-b-100-pure-ground-beef-chuck-80-lean-value-pack/635319")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.find("span", attrs = {"class":"sc-1xoyuqm-0 fbTxzd"})

print(quotes)



# pascal_source = untar_data(URLs.PASCAL_2007)
# df = pd.read_csv(pascal_source/"train.csv")

# pascal = DataBlock(blocks=(ImageBlock, MultiCategoryBlock),
#                    splitter=ColSplitter(),
#                    get_x=ColReader(0, pref=pascal_source/"train"),
#                    get_y=ColReader(1, label_delim=' '),
#                    item_tfms=Resize(224),
#                    batch_tfms=aug_transforms())