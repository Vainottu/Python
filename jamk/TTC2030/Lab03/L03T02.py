#Tee ohjelma, joka kysyy käyttäjältä 3 kokonaislukua ja tulostaa niistä suurimman.



numero1 = int(input("Syötä ensimmäinen kokonaisluku: "))
numero2 = int(input("Syötä toinen kokonaisluku: "))
numero3 = int(input("Syötä kolmas kokonaisluku: "))

if numero1 > numero2 and numero1 > numero3:
    print("Suurin luku on:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Suurin luku on:", numero2)
else:
    print("Suurin luku on:", numero3)
