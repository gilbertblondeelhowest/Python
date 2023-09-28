#oef3 Vraag aan de gebruiker naam, voornaam en leeftijd op.
#Print nadien in omgekeerde volgorde alles op één lijn af.
#Gebruik hiervoor de formated-string.




# str(string) of int(integer) is niet noodzakelijk in dit geval (input("xxxx"))
naam = str(input("Geef je naam op:>"))
voornaam = str(input("Geef je voornaam op:>"))
leeftijd = int(input("Geef je leeftijd op:>"))

print(f" Je bent {leeftijd} en je naam is {voornaam} {naam} ")