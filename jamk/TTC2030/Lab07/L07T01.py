#Tee luokka Pelikortti. Luokalla on kaksi ominaisuutta: maa ja arvo. Maa on: pata, hertta, ruutu tai risti. Arvo on jokin luku 2-14.
#Luokan ei tarvitse kuitenkaan mitenkään tarkista että olion ominaisuudet ovat edellä mainitut. Luo viisi Pelikortti-oliota erilaisilla ominaisuuksilla.
#Näytä korttien tiedot esimerkiksi seuraavasti print(kortti1.maa , kortti1.arvo).



class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

# Luodaan viisi Pelikortti-oliota erilaisilla ominaisuuksilla
kortti1 = Pelikortti("pata", 10)
kortti2 = Pelikortti("hertta", 3)
kortti3 = Pelikortti("ruutu", 14)
kortti4 = Pelikortti("risti", 7)
kortti5 = Pelikortti("pata", 2)

# Tulostetaan korttien tiedot
print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)
