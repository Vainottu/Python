#Tee ohjelma jossa annetaan oppilaalle arvosana alla olevan taulukon mukaan. Kysy pistemäärä konsolissa ja tulosta arvosana.


pistemäärä = int(input("Anna pistemäärä: "))

if pistemäärä >= 0 and pistemäärä <= 1:
    arvosana = 0
elif pistemäärä >= 2 and pistemäärä <= 3:
    arvosana = 1
elif pistemäärä >= 4 and pistemäärä <= 5:
    arvosana = 2
elif pistemäärä >= 6 and pistemäärä <= 7:
    arvosana = 3
elif pistemäärä >= 8 and pistemäärä <= 9:
    arvosana = 4
elif pistemäärä >= 10 and pistemäärä <= 12:
    arvosana = 5
else:
    print("Virheellinen pistemäärä.")
    arvosana = None

if arvosana is not None:
    print("Arvosana on:", arvosana)
