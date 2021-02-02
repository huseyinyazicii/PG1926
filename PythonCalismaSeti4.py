kontrol = ""
liste = []
while True:
    kontrol = input("Sayı giriniz : (çıkış için 'q')")
    if kontrol == "q":
        break
    liste.append(int(kontrol))

print(liste)

liste.sort()
liste.reverse()

for i in liste:
    if i%2 == 1:
        print("En büyük tek sayı : {}".format(i))
        break
