#Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja ja tallentaa annetut luvut tiedostoon luvut.txt.
#Ohjelma lopettaa lukujen kysymisen, kun käyttäjä antaa tyhjän syötteen. Viimeiseksi ohjelma kirjoittaa tiedostoon montako lukua käyttäjä antoi seuraavasti:
#Syötetty 5 lukua. Tarkista lopuksi tiedoston sisältö tekstieditorilla.



tiedoston_nimi = "luvut.txt"
lukumaara = 0

try:
    with open(tiedoston_nimi, "w") as tiedosto:
        while True:
            syote = input("Anna kokonaisluku (tyhjä lopettaa): ")
            if syote == "":
                break
            try:
                luku = int(syote)
                tiedosto.write(str(luku) + "\n")
                lukumaara += 1
            except ValueError:
                print("Syöte ei ollut kokonaisluku!")

    tiedosto.write("Syötetty " + str(lukumaara) + " lukua.")
    print("Tallennettu tiedostoon", tiedoston_nimi)
    print("Syötit", lukumaara, "lukua.")

except Exception as e:
    print("Tapahtui virhe tiedoston käsittelyssä: ", str(e))
