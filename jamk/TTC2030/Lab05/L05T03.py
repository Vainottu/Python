#Tee funktio average(), jolle viedään 3 parametria. Average funktio palauttaa annettujen parametrien keskiarvon yhden desimaalin tarkkuudella.



def average(a, b, c):
    avg = (a + b + c) / 3
    return round(avg, 1)


result = average(5, 10, 15)
print(result) # tulostaa 10.0

