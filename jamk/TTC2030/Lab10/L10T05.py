#Tee ohjelma, jolla yrität kirjoittaa tekstitiedoston 'ayho.txt' (sisällön saat päättää itse) Windows-koneen kovalevyn C:n juureen (macOS/Linux/Unix-koneilla käyttäjän juurihakemistoon).
#Mitä tapahtui? Kaatuiko ohjelma virheeseen? Korjaa ohjelma niin, ettei se kaadu, eli lisää siihen tarvittava poikkeustenkäsittely.





#Ohjelma kaatuu virheeseen, jos yrität kirjoittaa tiedoston juurihakemistoon, sillä sinulla ei välttämättä ole siihen oikeuksia.
#Windows-koneessa voit saada virheilmoituksen "PermissionError: [Errno 13] Permission denied: 'C:\ayho.txt'" ja muilla käyttöjärjestelmillä vastaavasti.



import os

try:
    # Avaa tiedosto kirjoitustilassa
    file = open(os.path.join("C:\\", "ayho.txt"), "w")
    
    # Kirjoita viisi rekisterinumeroa tiedostoon
    for i in range(5):
        reg_number = input(f"Syötä rekisterinumero {i+1}: ")
        file.write(reg_number + "\n")
    
    # Sulje tiedosto
    file.close()
    print("Tiedoston kirjoitus onnistui!")
    
except IOError:
    print("Tiedostoon kirjoitus epäonnistui.")
