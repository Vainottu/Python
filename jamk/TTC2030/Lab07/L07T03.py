#Tee luokka Cat. Tee Cat-luokalle kaksi ominaisuutta name ja color, sekä yksi metodi miau. Luo Cat-luokasta kaksi erilaista kissa-oliota seuraavilla tiedoilla:
#name: Kit, color: black
#name: Kat, color: white

#Kissat sanovat naukuessaan: Meoooooow!

#Näytä kissa-olioiden ominaisuudet konsolille, laita kissat myös naukumaan:


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def miau(self):
        print("Meoooooow!")

# Luodaan kaksi Cat-oliota
kit = Cat("Kit", "black")
kat = Cat("Kat", "white")

# Tulostetaan kissa-olioiden ominaisuudet
print("Kissan nimi: ", kit.name)
print("Kissan väri: ", kit.color)
print("Kissan nimi: ", kat.name)
print("Kissan väri: ", kat.color)

# Kutsumme miau-metodia kummallekin kissalle
print(kit.miau())
print(kat.miau())
