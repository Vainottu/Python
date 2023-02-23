#Tee ohjelma, joka kysyy käyttäjän kokonimen. Tämän jälkeen ohjelma erottaa annetusta merkkijonosta välilyönnin perusteella käyttäjän etu- ja sukunimen.
#Vinkki 1: Merkkijono muuttujasta nimi voi hakea välilyönnin paikan seuraavalla funktiolla.
#i = nimi.find(' ')
#Vinkki 2: Voit palauttaa merkkijonosta halutun osan käyttämällä slice-syntaksia. Määritä aloitusindeksi ja loppuindeksi kaksoispisteellä erotettuina palauttaaksesi osan merkkijonosta.


nimi = input("Syötä koko nimesi: ")

# Etsi ensimmäinen välilyönti
vali = nimi.find(" ")
if vali == -1:
    print("Virhe: Syötä koko nimesi (etu- ja sukunimi)!")
else:
    etunimi = nimi[:vali]
    sukunimi = nimi[vali+1:]
    print("Etu- ja sukunimesi ovat", etunimi, "ja", sukunimi)
