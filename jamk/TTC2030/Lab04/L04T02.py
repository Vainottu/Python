#Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän.
#Sademäärä annetaan kokonaislukuna, jollei kyseisenä päivänä ole satanut käyttäjä antaa luvuksi 0. Laske ja näytä viikon kokonaissademäärä.


sade = []
viikon_sademäärä = 0

for i in range(7):
    sademaara = int(input(f"Anna päivän {i+1} sademäärä millimetreinä (0 jos ei satanut): "))
    sade.append(sademaara)
    viikon_sademäärä += sademaara

print(f"Viikon kokonaissademäärä oli {viikon_sademäärä} millimetriä.")
