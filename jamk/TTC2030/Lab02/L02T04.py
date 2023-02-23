#Tee ohjelma, joka kysyy käyttäjän etunimen ja syntymävuoden.
# Tämän jälkeen ohjelma laskee montako vuotta käyttäjä on (syntymäpäivää ja -kuukautta ei tarvitse huomioida)
# Tämän jälkeen ohjelma kertoo kuinka vanha käyttäjä on.

#
from datetime import date

nimi = input("Syötä etunimesi: ")
syntymavuosi = int(input("Syötä syntymävuotesi: "))

nykyinen_vuosi = date.today().year
ika = nykyinen_vuosi - syntymavuosi

print(nimi + ", olet " + str(ika) + " vuotta vanha.")
