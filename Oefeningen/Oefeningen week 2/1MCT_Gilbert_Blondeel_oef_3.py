from datetime import datetime #<--------- nodig om datum te gebruike


#ex 3
geboortejaar = int(input("Geef jouw geboortejaar op:>"))
geboortemaand = int(input("Geef jouw geboortemaand op:>"))

#jaartal van vandaga opvrage

huidige_datum = datetime.now()
huidige_jaartal = huidige_datum.year
huidige_maand = huidige_datum.month
leeftijd = huidige_jaartal - geboortejaar

if leeftijd > 18:
    print("U mag alcohol drinken")
elif leeftijd == 18 and huidige_maand > geboortemaand:
    print("U mag alcohol drinken")
else:
    print("U mag helaas nog geen alcohol drinken...")

