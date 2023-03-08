#Tee ohjelma, joka kysyy ensin käyttäjältä jonkin luvun väliltä 1-10. Tämän jälkeen näytä luvut yhdestä annettuun lukuun ja luvun neliön.


n = int(input("Anna luku väliltä 1-10: "))

for i in range(1, n+1):
    print(f"{i} {i*i}")
