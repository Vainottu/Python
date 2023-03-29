#Tee ohjelma joka kysyy käyttäjältä kurssien arvosanoja (arvosana on kokonaisuluku 0,1,2,3,4 tai 5) ja tallentaa ne listaan.
#Käyttäjä voi syöttää niin monta kurssiarvosanaa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä.
#Näytä lopuksi montako arvosanaa käyttäjä antoi ja arvosanojen keskiarvo.


grades = []
while True:
    grade = input("Syötä arvosana (0-5): ")
    if not grade:
        break
    grade = int(grade)
    if grade < 0 or grade > 5:
        print("Virheellinen arvosana, yritä uudelleen.")
    else:
        grades.append(grade)

if len(grades) == 0:
    print("Et antanut yhtään arvosanaa.")
else:
    average = sum(grades) / len(grades)
    print("Antamiesi arvosanojen määrä:", len(grades))
    print("Arvosanojen keskiarvo:", average)
