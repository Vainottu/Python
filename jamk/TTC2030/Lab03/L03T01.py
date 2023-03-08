#Tee ohjelma, joka kysyy käyttäjältä kaksi kokonaislukua ja tulostaa niistä pienemmän.

numero1 = int(input("Syötä ensimmäinen kokonaisluku: "))
numero2 = int(input("Syötä toinen kokonaisluku: "))

if numero1 < numero2:
    print("Pienempi luku on:", numero1)
else:
    print("Pienempi luku on:", numero2)
