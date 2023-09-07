# Luodaan tyhjä tuoterekisteri sanakirja, jossa avaimena on tuotteen nimi ja arvona hinta.
tuoterekisteri = {}

# Funktio lisää tuotteen rekisteriin.
def lisaa_tuote():
    nimi = input("Syötä tuotteen nimi: ")
    hinta = float(input("Syötä tuotteen hinta: "))
    tuoterekisteri[nimi] = hinta
    print(f"{nimi} on lisätty rekisteriin hintaan {hinta} €.")

# Funktio poistaa tuotteen rekisteristä.
def poista_tuote():
    nimi = input("Syötä poistettavan tuotteen nimi: ")
    if nimi in tuoterekisteri:
        del tuoterekisteri[nimi]
        print(f"{nimi} on poistettu rekisteristä.")
    else:
        print(f"{nimi} ei ole rekisterissä.")

# Funktio tulostaa kaikki tuotteet ja niiden hinnat nousevassa tai laskevassa järjestyksessä.
def tulosta_tuotteet(nousevassa_jarjestyksessa=True):
    jarjestetty_rekisteri = sorted(tuoterekisteri.items(), key=lambda x: x[1], reverse=not nousevassa_jarjestyksessa)
    for nimi, hinta in jarjestetty_rekisteri:
        print(f"{nimi}: {hinta} €")

# Funktio tallentaa tuoterekisterin tekstitiedostoon.
def tallenna_tiedostoon():
    tiedostonimi = input("Syötä tiedoston nimi tallentamista varten: ")
    with open(tiedostonimi, "w") as tiedosto:
        for nimi, hinta in tuoterekisteri.items():
            tiedosto.write(f"{nimi}: {hinta}\n")
    print("Tuoterekisteri tallennettu tiedostoon.")

# Funktio avaa tallennetun tekstitiedoston ja lisää tuotteet takaisin rekisteriin.
def avaa_tiedosto():
    tiedostonimi = input("Syötä tiedoston nimi avattavaksi: ")
    try:
        with open(tiedostonimi, "r") as tiedosto:
            for rivi in tiedosto:
                nimi, hinta = rivi.strip().split(": ")
                tuoterekisteri[nimi] = float(hinta)
        print("Tiedosto avattu ja tuotteet lisätty rekisteriin.")
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")

# Funktio näyttää kysytyn tuotteen hinnan.
def nayta_tuotteen_hinta():
    nimi = input("Syötä tuotteen nimi, jonka hintaa haluat nähdä: ")
    if nimi in tuoterekisteri:
        hinta = tuoterekisteri[nimi]
        print(f"{nimi} hinta on {hinta} €.")
    else:
        print(f"{nimi} ei ole rekisterissä.")

# Pääohjelma
while True:
    print("\nValitse toiminto:")
    print("1. Lisää tuote")
    print("2. Poista tuote")
    print("3. Tulosta tuotteet (nousevassa järjestyksessä)")
    print("4. Tulosta tuotteet (laskevassa järjestyksessä)")
    print("5. Tallenna tuoterekisteri tiedostoon")
    print("6. Avaa tallennettu tiedosto")
    print("7. Näytä tuotteen hinta")
    print("8. Lopeta ohjelma")
    
    valinta = input("Valintasi (1-8): ")
    
    if valinta == "1":
        lisaa_tuote()
    elif valinta == "2":
        poista_tuote()
    elif valinta == "3":
        tulosta_tuotteet()
    elif valinta == "4":
        tulosta_tuotteet(nousevassa_jarjestyksessa=False)
    elif valinta == "5":
        tallenna_tiedostoon()
    elif valinta == "6":
        avaa_tiedosto()
    elif valinta == "7":
        nayta_tuotteen_hinta()
    elif valinta == "8":
        print("Ohjelma lopetetaan.")
        break
    else:
        print("Virheellinen valinta. Valitse uudelleen.")
