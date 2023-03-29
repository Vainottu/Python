#Lataa tämä tekstitiedosto nimet.txt koneellesi.
#Tiedostossa on henkilöitten nimiä. Sama nimi saattaa esiintyä monta kertaa.
#Tee ohjelma, joka lukee em. tekstitiedostosta nimet ja kertoo montako nimeä löytyy ja montako kertaa kukin nimi esiintyy. Käytä Dictionary-kokoelmaa ratkaisussasi.



with open("nimet.txt") as f:
    names = f.read().splitlines()

name_count = {}
for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print("Löytyi", len(name_count), "eri nimeä.")

for name, count in name_count.items():
    print(name, "esiintyy", count, "kertaa.")
