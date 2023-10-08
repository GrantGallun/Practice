#remove digit from 10 digit minimum number 
valid = False
validbig=""
while valid==False:
    bigno = input("enter a number more than 10 digi: ")
    listbig = list(bigno)
    if len(listbig)<10:
        print("less than 10 digi")
        continue
    valid=True
    validbig=bigno
listbig=list(validbig)

digitR = int(input("Please enter digit to remove"))
listbig.remove(str("digitR"))

