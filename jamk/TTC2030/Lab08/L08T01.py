#Tee ohjelma, joka kysyy käyttäjältä kymmenen kaverin nimen.
#Ohjelma näyttää ensin kaverit annetussa järjestyksessä.
#Seuraavaksi ohjelma näyttää kaverit käännetyssä järjestyksessä, eli viimeiseksi annetun ensimmäisenä jne.


# Pyydä käyttäjältä kymmenen kaverin nimi ja tallenna ne listalle
kaverit = []
for i in range(10):
    nimi = input("Syötä kaverin nimi: ")
    kaverit.append(nimi)

# Tulosta kaverit annetussa järjestyksessä
print("Kaverit annetussa järjestyksessä:")
for nimi in kaverit:
    print(nimi)

# Tulosta kaverit käännetyssä järjestyksessä
print("Kaverit käännetyssä järjestyksessä:")
kaverit.reverse()
for nimi in kaverit:
    print(nimi)
