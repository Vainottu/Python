#Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. Lisää luokalle str metodi.
#Luokan str metodi toimii kuten on alla esitetty. Luo kaksi Human-luokan oliota seuraavilla tiedoilla:
#Nimi: Adam, ikä: 19
#Nimi: Eva, ikä: 18


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} vuotta"



# Luodaan kaksi Human-oliota
adam = Human("Adam", 19)
eva = Human("Eva", 18)

# Tulostetaan olion tiedot käyttäen __str__ metodia


print(adam)
print(eva)
