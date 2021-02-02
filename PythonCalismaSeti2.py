def checkIt(length,mail):
    x = False
    y = 0
    k = 0
    for i in range(0,len(mail)):
        if mail[i] == "@":
            x = True
            y = i
            break
    for i in range(y,len(mail)):
        if mail[i] == ".":
            k = k + 1
    if k != length:
        x = False
    if length > 3:
        x = False
    return (x)
        

length = input("Uzunluk Giriniz : ")
mail = input("Mail Adresinizi Giriniz : ")

if checkIt(length,mail) == True:
    print("Mailiniz Uygundur")
else:
    print("Mailiniz Uygun Değildir")


