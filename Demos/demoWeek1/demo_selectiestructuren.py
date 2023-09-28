getal = int(input("Geef uw score op:"))

#selectiestructuur ==> iets uitvoeren wanneer een voorwaarde voldaan is
if getal >= 10:
    print("U bent geslaagd")
    print("Tof, daar drinken we meerdere Omers op")
else:
    print("u bent (nog) niet geslaagd")
    print("Laat ons even bekomen met een duvel")

# indien slechts één commando -> gebruik dan 1 lijn
if getal == 20: print("Proficiat met uw score!")

# verschillende soorten vergelijkingsoperatoren
getal = 10
if getal>10: print("Getal is verschillend van 0")
if getal == 0: print("Getal is verschillend van 0")

# koppelen van voorwaarden via booleaanse operatoren
getal = 17
if (getal >= 16) and (getal <= 20): print("Grote onderscheiding")

if (getal == 0) or (getal == 1): print("getal is 0 of 1")

if not ((getal % 2) == 0): print("getal is oneven")

