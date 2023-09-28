# Herhaling selectiestructuren

getal = int(input("Geef uw score op:"))

# ENKELVOUDIGE SELECTIE
if getal > 10:
    print("Je bent geslaagd!")
if getal != 20:
    print("Je behaalde nog niet het maximum")

# TWEEVOUDIGE SELECTIE
if getal >= 10:
    print("u bent geslaagd")
    print("tof, daar drinken we meerdere op")
else:
    print("u bent niet geslaagd")
    print("kom maar nog ne keer af")


# MEERVOUDIGE SELECTIE
if getal >= 16:
    print("Uitzonderlijk!")
elif getal >= 14:
    print("Zeer goed!")
elif getal >= 12:
    print("Goed!")
elif getal >= 10:
    print("Voldoende!")
else:
    print("Onvoldoende")


if getal >= 18 and getal <= 20:
    print("Grootste onderscheiding")

if getal == 0 or getal == 1:
    print("getal is 0 of 1")

if not ((getal % 2) == 0):
    print("getal is oneven")

if not getal % 2 == 0:
    print("getal is oneven")
