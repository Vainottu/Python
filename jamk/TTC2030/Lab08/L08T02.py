#Toteuta ohjelma, joka kysyy käyttäjältä autojen rekisterinumeroita (siis esim 'ABC-123' jne) ja tallentaa ne listaan.
#Käyttäjä voi syöttää niin monta rekisterinumeroa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä. Näytä syötetyt rekisterinumero aakkosjärjestyksessä.



rekisterinumerot = []

while True:
    numero = input("Syötä rekisterinumero: ")
    if numero == "":
        break
    rekisterinumerot.append(numero)

rekisterinumerot.sort()
print("Rekisterinumerot aakkosjärjestyksessä:")
for numero in rekisterinumerot:
    print(numero)
