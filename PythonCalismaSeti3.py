kontrol = ""
liste = []
while True:
    kontrol = input("Sayı giriniz : (çıkış için 'q')")
    if kontrol == "q":
        break
    liste.append(int(kontrol))

print(liste)

sayac = 0
for i in liste:
    sayac = sayac + 1
    if i == 0:
        liste.insert(0,0)
        liste.pop(sayac)

print(liste)


    
