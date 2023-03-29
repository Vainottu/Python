#Tee ohjelma, joka kysyy käyttäjältä henkilöiden sukunimiä ja kirjoittaa käyttäjän antamat nimet tiedostoon.
#Nimiä kysytään niin kauan kunnes käyttäjä antaa tyhjän syötteen. Huomioi mahdolliset poikkeukset, joita tiedoston käsittely voi aiheuttaa.


tiedoston_nimi = "sukunimet.txt"

# Avaa tiedosto tiedoston_luomis_tilassa, jotta se tyhjennetään ensin
with open(tiedoston_nimi, "w") as tiedosto:
    pass

# Kysy käyttäjältä sukunimiä ja kirjoita ne tiedostoon
while True:
    sukunimi = input("Anna sukunimi (tyhjä lopettaa): ")
    if not sukunimi:
        break
    try:
        with open(tiedoston_nimi, "a") as tiedosto:
            tiedosto.write(sukunimi + "\n")
    except Exception as e:
        print("Tapahtui virhe tiedoston kirjoituksessa: ", str(e))
        break
