#Tee ohjelma, joka kysyy käyttäjältä kuinka monta kokonaislukua luodaan.
#Lisää listaan luvut niin että alkion arvo on alkion indeksi kertaa 10. Huomaa, että indeksit alkavat nollasta (0). Tulosta taulukon sisältö konsoliin.



n = int(input("Kuinka monta kokonaislukua haluat luoda? "))
lista = [i*10 for i in range(n)]
print(lista)
