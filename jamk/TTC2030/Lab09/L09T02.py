#Jatkoa edelliseen. Tee ohjelma, joka lukee edellisessä tehtävässä luodusta tiedostosta nimet ja näyttää ne konsolilla.
#Tämän jälkeen ohjelma lajittelee nimet aakkosjärjestykseen ja näyttää ne konsolilla aakkosjärjestyksessä.







tiedoston_nimi = "sukunimet.txt"

# Lue tiedostosta nimet ja näytä ne konsolilla
try:
    with open(tiedoston_nimi, "r") as tiedosto:
        nimet = tiedosto.read().splitlines()
        print("Tiedostosta luettiin seuraavat nimet:")
        for nimi in nimet:
            print(nimi)
except Exception as e:
    print("Tapahtui virhe tiedoston lukemisessa: ", str(e))

# Lajittele nimet aakkosjärjestykseen ja näytä ne konsolilla
nimet.sort()
print("Nimet aakkosjärjestyksessä:")
for nimi in nimet:
    print(nimi)
