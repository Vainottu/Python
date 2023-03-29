#Tee funktio get_fuel(), jolle viedään 2 parametria.
#Funktio laskee ja palauttaa automatkaan kuluneen polttoaineen määrän.
#Ensimmäinen parametri on ajetut kilometrit, toinen parametri on keskikulutus 100 km kohti.
#Funktio palauttaa merkkijonona kulutuksen yhden desimaalin tarkkuudella seuraavassa muodossa 15.2 ltr.




def get_fuel(km, consumption):
    fuel = km * (consumption / 100)
    return f"{fuel:.1f} ltr"


result = get_fuel(500, 7.5)
print(result) # tulostaa "37.5 ltr"

