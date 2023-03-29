#Lataa oheinen tiedosto names.txt omalle koneellesi. Lisää tiedostoon oma nimesi viimeiseksi. Tee ohjelma, joka lukee tiedoston nimet ja ilmoittaa:
#a) montako nimeä tiedostossa on b) mikä nimistä on pisin
#Käytä poikkeustenkäsittelyä.



try:
    with open("names.txt", "r") as file:
        names = file.readlines()
        name_count = len(names)
        longest_name = max(names, key=len).strip()
        print(f"Tiedostossa on {name_count} nimeä.")
        print(f"Pisin nimi on: {longest_name}")
except FileNotFoundError:
    print("Tiedostoa ei löydy.")
except Exception as e:
    print(f"Virhe: {e}")
