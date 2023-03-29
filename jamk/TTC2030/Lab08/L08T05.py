#Tee funktio lotto(), joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja palauttaa sen merkkijonona, luvut eroteltuna pilkuilla.
#Siis esimerkiksi näin: 1,3,5,10,20,33,39
#Käytä lukujen arpomiseen Pythonin valmista modulia random ja sen metodia randint, kts lisää: https://www.w3schools.com/python/gloss_python_random_number.asp



import random

def lotto():
    numerot = []
    while len(numerot) < 7:
        uusi_numero = random.randint(1, 40)
        if uusi_numero not in numerot:
            numerot.append(uusi_numero)
    numerot.sort()
    return ",".join(str(numero) for numero in numerot)

# Testataan funktiota
print(lotto())
