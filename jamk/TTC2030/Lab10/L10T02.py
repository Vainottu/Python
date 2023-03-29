#Tee ohjelma joka näyttää onko annettu vuosi karkausvuosi.
#Vuosiluku kysytään käyttäjältä. Algoritmi: 4:llä jaolliset on, paitsi täydet vuosisadat.
#Kuitenkin 400:lla jaolliset vuosisadat ovat karkausvuosia. Esim. 1991 -> ei, 1992 -> on, 1900 -> ei, 2000 -> on



vuosi = int(input("Syötä vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or vuosi % 400 == 0:
    print(vuosi, "on karkausvuosi.")
else:
    print(vuosi, "ei ole karkausvuosi.")
