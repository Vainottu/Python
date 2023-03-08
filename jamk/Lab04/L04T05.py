#Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen. Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia. Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä järjestyksessä.
#Siis esimerkiksi jos käyttäjä antaa etunimekseen 'Kirsi' ja sukunimeksi 'Kernell' suoritus olisi:



etu_nimi = input("Anna etunimi: ")
suku_nimi = input("Anna sukunimi: ")

# Tulostetaan etunimen ensimmäinen kirjain etunimen pituuden verran
for i in range(len(etu_nimi)):
    print(etu_nimi[0], end="")
print()

# Tulostetaan sukunimi käänteisessä järjestyksessä
print(suku_nimi[::-1])
