#oef5 Vraag aan de gebruiker het aantal dagen, uren, minuten en seconden op.
#Bepaal het totale aantal seconden.


aantal_dagen = int(input("Geef het aantal dagen op:>"))
aantal_uren = int(input("Geef het aantal uren op:>"))
aantal_minuten = int(input("Geef het aantal minuten op:>"))
aantal_seconden = int(input("Geef het aantal seconden op:>"))
totale_seconden = (aantal_dagen*24*60*60)+(aantal_uren*60*60)+(aantal_minuten*60)+(aantal_seconden)

print(f" Het totale aantal seconden bedraagt: {totale_seconden} ")