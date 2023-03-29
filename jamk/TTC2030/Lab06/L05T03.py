#Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen.
#Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.




oppilaat = []
while True:
    nimi = input("Syötä oppilaan nimi (tyhjä lopettaa): ")
    if nimi == "":
        break
    oppilaat.append(nimi)

print("Annoit", len(oppilaat), "nimeä:", ", ".join(oppilaat))
