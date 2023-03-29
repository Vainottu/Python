#Tee ohjelma, joka arpoo lottorivejä ja tallentaa ne tekstitiedostoon 'lotto.txt'.
#Arvottu rivi sisältää seitsemän (7) numeroa väliltä 1-40. Käyttäjältä kysytään montako riviä arvotaan.
#Varmista arpoessasi riviä, että sama numero ei esiinny kahta kertaa.



import random

# Kysytään käyttäjältä montako riviä arvotaan
num_lines = int(input("Montako riviä arvotaan? "))

# Avataan tiedosto lotto.txt kirjoitustilassa
with open("lotto.txt", "w") as f:

    # Arvotaan pyydetty määrä rivejä
    for i in range(num_lines):
        # Arvotaan 7 numeroa väliltä 1-40 ilman toistoa
        lotto_row = random.sample(range(1, 41), 7)
        lotto_row.sort()

        # Tallennetaan arvottu rivi tiedostoon
        f.write(" ".join(str(n) for n in lotto_row) + "\n")

print("Arvotut rivit tallennettu tiedostoon lotto.txt.")
