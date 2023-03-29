#Tee ohjelma, jossa kysytään käyttäjältä tämän syntymävuoden. Annetun syntymävuoden perusteella laske henkilön ikä. Jotta ohjelmasi toimisi oikein myös tulevina vuosina, hae kuluva vuosi tietokoneen kellosta, eli käytä esim datetime.date.today()-metodia. Tee ohjelmaan funktio kerro3(age), joka iän perusteella palauttaa seuraavan tekstin:
#- jos ikä on alle 1 vuotta, palautetaan "baby"
#- jos ikä on alle 13 vuotta, palautetaan "child"
#- jos ikä on 13-19 vuotta, palautetaan "teen"
#- jos se on 20-65 vuotta, palautetaan "adult"
#- muussa tapauksessa palautetaan "senior".Tee ohjelma, jossa kysytään käyttäjältä tämän syntymävuoden. Annetun syntymävuoden perusteella laske henkilön ikä. Jotta ohjelmasi toimisi oikein myös tulevina vuosina, hae kuluva vuosi tietokoneen kellosta, eli käytä esim datetime.date.today()-metodia. Tee ohjelmaan funktio kerro3(age), joka iän perusteella palauttaa seuraavan tekstin:
#- jos ikä on alle 1 vuotta, palautetaan "baby"
#- jos ikä on alle 13 vuotta, palautetaan "child"
#- jos ikä on 13-19 vuotta, palautetaan "teen"
#- jos se on 20-65 vuotta, palautetaan "adult"
#- muussa tapauksessa palautetaan "senior".



import datetime

def kerro3(age):
    if age < 1:
        return "baby"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teen"
    elif age < 66:
        return "adult"
    else:
        return "senior"

syntymavuosi = int(input("Syötä syntymävuosi: "))
nykyinen_vuosi = datetime.date.today().year
ika = nykyinen_vuosi - syntymavuosi

print("Ikäsi on", ika, "vuotta, joten olet", kerro3(ika))
