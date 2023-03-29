#Tee funktio get_cost(), jolle viedään 3 parametria. Funktio laskee ja palauttaa automatkan polttoaineen hinnan.
#Ensimmäinen parametri on ajetut kilometrit, toinen parametri on keskikulutus 100 km kohti ja kolmas parametri on polttoaineen litrahinta.
#Funktio palauttaa kustannuksen merkkijonona kahden desimaalin (eli sentin tarkkuudella) seuraavassa muodossa 14.10 €



def get_cost(km, consumption, price_per_liter):
    fuel = km * (consumption / 100)
    cost = fuel * price_per_liter
    return f"{cost:.2f} €"



result = get_cost(500, 7.5, 1.45)
print(result) # tulostaa "40.69 €"
