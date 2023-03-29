#Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot.
#Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda).
#Keksi itse erilaisia rekisterinumeroita ja automerkkejä. Tallenna tiedot valitsemaasi Dictionary-kokoelmaan.
#Käytä rekisterinumeroa avaimena. Tulosta sen jälkeen autot aakkosjärjestyksessä rekisterinumeron mukaan.


autot = {
    "ABC-123": "Skoda",
    "DEF-456": "Toyota",
    "GHI-789": "Volvo",
    "JKL-012": "Honda",
    "MNO-345": "Ford",
    "PQR-678": "Audi",
    "STU-901": "BMW",
    "VWX-234": "Mercedes-Benz",
    "YZA-567": "Tesla",
    "BCD-890": "Kia"
}

# Tulosta sanakirjan avaimet aakkosjärjestyksessä
for avain in sorted(autot.keys()):
    print(avain + ": " + autot[avain])
