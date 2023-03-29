#Mäkihypyssä käytetään viittä arvostelutuomaria.
#Jokainen antaa hypylle pisteitä yhdestä kahteenkymmeneen 1-20.
#Kirjoita ohjelma, joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten, että summasta on vähennetty pois pienin ja suurin tyylipiste.




pisteet = []
for i in range(5):
    while True:
        piste = int(input("Anna pisteet tuomarilta {}: ".format(i+1)))
        if piste >= 1 and piste <= 20:
            break
        else:
            print("Pisteiden täytyy olla välillä 1-20.")
    pisteet.append(piste)

pisteet_summa = sum(pisteet)
pisteet_summa -= min(pisteet)
pisteet_summa -= max(pisteet)

print("Tyylipisteiden summa on", pisteet_summa)

