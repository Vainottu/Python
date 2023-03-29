#Tee funktio showtime(), joka muuttaa parametrinä saadun sekuntiarvon merkkijonoksi muotoon tunnit:minuutit:sekunnit. Funktio palauttaa seuraavasti:
# jos tunteja alle kymmenen muodossa 02:46:40 - jos tunteja yli kymmenen muodossa 12:46:40
#Sama myös minuuteissa.


def showtime(seconds):
    hours, remaining = divmod(seconds, 3600)
    minutes, seconds = divmod(remaining, 60)
    if hours < 10:
        hours = f"0{hours}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if hours < 12:
        return f"{hours}:{minutes}:{seconds}"
    else:
        return f"{hours-12}:{minutes}:{seconds}"


#kutsutaan func
result = showtime(10000)
print(result) # tulostaa "02:46:40"
