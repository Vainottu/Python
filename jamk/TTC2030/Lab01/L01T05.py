#Tee ohjelma, joka kysyy käyttäjältä ensin montako euroa hänelle on.
# Sen jälkeen kysy montako senttiä käyttäjällä on. Sen jälkeen näytä paljonko käyttäjällä on rahaa.
# Muistathan että sentti on euron sadasosa.


eurot = int(input("Kuinka monta euroa sinulla on? "))
sentit = int(input("Kuinka monta senttiä sinulla on? "))

raha = eurot + sentit / 100.0

print("Sinulla on yhteensä", raha, "euroa.")