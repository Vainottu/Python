#Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun.
#Annetun luvun perusteella ohjelma toimii seuraavasti: - jos luku on 10 tai 20, palauta teksti "Luku on 10 tai 20" - jos luku on 100 tai 200, palauta teksti "Luku on 100 tai 200" - muuten palauta annettu luku tekstinä, siis esim "Luku on 1".


luku = int(input("Syötä kokonaisluku: "))

if luku == 10 or luku == 20:
    print("Luku on 10 tai 20")
elif luku == 100 or luku == 200:
    print("Luku on 100 tai 200")
else:
    print("Luku on", luku)
