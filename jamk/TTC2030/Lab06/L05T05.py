#Tuuma (engl. inch) on Brittiläisessä imperiumissa ja USA:ssa käytetty pituusmitta.
#Yksi tuuma on 2.54 senttimetriä. Tee funktio show_cm, joka näyttää parametrina annetun tuumamitan sentteinä seuraavassa muodossa 2 tuumaa on 5,08 cm.






def show_cm():
    while True:
        try:
            tuumat = float(input("Syötä tuumamitta: "))
            sentit = tuumat * 2.54
            print("{:.2f} tuumaa on {:.2f} cm.".format(tuumat, sentit))
            break
        except ValueError:
            print("Syötteen täytyy olla luku.")


show_cm()
