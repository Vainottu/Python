#Tee funktiot: celToFah() ja fahToCel()
#Funktiot ottavat parametrikseen asteluvun. Funktio celToFah() muuttaa celsius-asteet fahrenheitiksi.
#Ja funktio fahToCel() muuttaa fahrenheitit celsiuksiksi. Muutettu astearvo palautetaan yhden desimaalin tarkkuudella.
#Testaa kumpikin funktio kutsumalla sitä käyttäjän antamilla luvuilla.





#func
def celToFah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 1)

def fahToCel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 1)

#pyydetään käyttäjää syöttämään lämpötila celsius-asteina
celsius = float(input("Syötä lämpötila celsius-asteina: "))
fahrenheit = celToFah(celsius)
print(f"{celsius} celsius-astetta on {fahrenheit} fahrenheit-astetta.")

#pyydetään käyttäjää syöttämään lämpötila fahrenheit-asteina
fahrenheit = float(input("Syötä lämpötila fahrenheit-asteina: "))
celsius = fahToCel(fahrenheit)
print(f"{fahrenheit} fahrenheit-astetta on {celsius} celsius-astetta.")