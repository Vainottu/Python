#Autotallissasi on kolme autoa. Tee luokka Car. Car-luokalla on kolme ominaisuutta:
#brand, model ja price. Luo Car-luokasta vähintään kolme erilaista auto-oliota. Aseta autojen ominaisuudet seuraavasti:
#1) brand="Skoda" model="Octavia" price=3000 2) brand="Audi" model="A4" price=4000 3) brand="Volvo" model="V70" price=5000

#Tulosta kaikkien autotallin kolmen auton ominaisuudet konsolille. Laske myös autojen yhteishinta, ja näytä se konsolilla:







class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

# Luodaan kolme Car-oliota
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

# Tulostetaan autojen ominaisuudet konsolille
print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Price:", car1.price)

print("\nCar 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)
print("Price:", car2.price)

print("\nCar 3:")
print("Brand:", car3.brand)
print("Model:", car3.model)
print("Price:", car3.price)

# Lasketaan autojen yhteishinta
total_price = car1.price + car2.price + car3.price
print("\nTotal price of all cars:", total_price)
