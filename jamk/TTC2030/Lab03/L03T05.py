#Tee ohjelma, joka kysyy käyttäjältä viisi lukua. Laske annetuista luvuista yhteen ne luvut, jotka ovat nollaa suurempia. Siis jos käyttäjä antaa nollan tai negatiivisen luvun sitä ei lisätä summaan. Tulosta summa konsoliin. Kokeile ohjelmaasi esim seuraavilla arvoilla: 1,2,3,4,5 ja -2,0,2,4,6. Mitä sait summaksi?



luku1 = int(input("Syötä 1. luku: "))
luku2 = int(input("Syötä 2. luku: "))
luku3 = int(input("Syötä 3. luku: "))
luku4 = int(input("Syötä 4. luku: "))
luku5 = int(input("Syötä 5. luku: "))

summa = 0
if luku1 > 0:
    summa += luku1
if luku2 > 0:
    summa += luku2
if luku3 > 0:
    summa += luku3
if luku4 > 0:
    summa += luku4
if luku5 > 0:
    summa += luku5

print("Nollaa suurempien lukujen summa on:", summa)
