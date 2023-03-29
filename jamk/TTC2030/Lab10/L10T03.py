# Tee luokka account, jolla on ominaisuus saldo sekä metodit nostoa varten withdraw(money) ja tilille panoa varten add(money).
#Tilille voi lisätä rahaa, ja tililtä voi nostaa rahaa, mutta vain sen verran kun tilillä on saldoa.
#Tilin saldo ei voi olla negatiivinen, ja huom tarkistus täytyy tehdä luokan metodissa!

#Tee luokasta olio-muuttuja, johon alkusaldoksi lisäät aluksi on 2000€.
#Tulosta pankkitilin saldo konsoliin. Kysy konsolissa kuinka monta euroa lisätään saldoon.
#Lisää eurot saldoon ja näytä saldo konsolissa. Nosta sen jälkeen tililtä 1500€ ja näytä saldo. Koeta sen jälkeen nostaa tililtä uudestaan 1500€



class Account:
    def __init__(self, saldo):
        self.saldo = saldo

    def add(self, money):
        self.saldo += money
        print("Tilillesi lisättiin", money, "euroa.")
        print("Uusi saldo on", self.saldo, "euroa.")

    def withdraw(self, money):
        if self.saldo >= money:
            self.saldo -= money
            print("Tililtäsi nostettiin", money, "euroa.")
            print("Uusi saldo on", self.saldo, "euroa.")
        else:
            print("Tililläsi ei ole tarpeeksi rahaa.")

# Esimerkki luokan käytöstä:
tili = Account(2000)  # Luodaan olio-muuttuja tilille, jonka alkusaldo on 2000 euroa.
print("Tilin saldo on", tili.saldo, "euroa.")

lisays = int(input("Kuinka paljon haluat lisätä tilillesi? "))
tili.add(lisays)

nosto = int(input("Kuinka paljon haluat nostaa tililtäsi? "))
tili.withdraw(nosto)

nosto2 = int(input("Yritä nyt nostaa tililtäsi 1500 euroa: "))
tili.withdraw(nosto2)
