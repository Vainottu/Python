#Tee luokka Mobile. Mobile-luokalla on kolme ominaisuutta: brand, model ja price.
#Lisää luokalle konstruktori init jolla voidaan oliota luodessa asettaa edellä mainitut ominaisuudet.


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

# Luodaan kaksi Mobile-oliota
mobile1 = Mobile("Samsung", "Galaxy S21", 999)
mobile2 = Mobile("Apple", "iPhone 13", 1099)

# Tulostetaan mobiilien ominaisuudet konsolille
print("Mobile 1: ")
print("Brand: ", mobile1.brand)
print("Model: ", mobile1.model)
print("Price: ", mobile1.price)

print("\nMobile 2: ")
print("Brand: ", mobile2.brand)
print("Model: ", mobile2.model)
print("Price: ", mobile2.price)
