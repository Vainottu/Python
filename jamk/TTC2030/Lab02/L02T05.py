#Tee ohjelma, joka kysyy käyttäjän etunimen.
# Tämän jälkeen ohjelma laskee ja näyttää montako kirjainta etunimessä on.
# Ohjelma toistaa käyttäjän etunimen kirjainta niin monta kertaa kun etunimessä on kirjaimia.



nimi = input("Syötä etunimesi: ")
kirjaimia = len(nimi)

print("Etunimessäsi on", kirjaimia, "kirjainta.")
print(nimi * kirjaimia)
