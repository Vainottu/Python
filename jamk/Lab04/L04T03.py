#Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja. Lukuja kysytään siihen saakka kunnes käyttäjä antaa tyhjän syötteen.
#Laske kuinka monta lukua käyttäjä antoi, laske myös annettujen lukujen summa. Näytä annettujen lukujen lukumäärä ja summa käyttäjälle.


lukujen_summa = 0
lukujen_maara = 0

while True:
    luku_str = input("Anna kokonaisluku: ")
    if luku_str == "":
        break
    luku = int(luku_str)
    lukujen_summa += luku
    lukujen_maara += 1

print(f"Annoit {lukujen_maara} lukua, joiden summa on {lukujen_summa}.")
