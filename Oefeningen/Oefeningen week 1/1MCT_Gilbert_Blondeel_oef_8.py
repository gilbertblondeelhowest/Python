#oef 8 Vraag aan de gebruiker twee int-getallen (gehele getallen) op.
#Bereken nu volgend resultaat: (x + y) * (x + y)

getal1 = int(input("Geef een getal op:>"))
getal2 = int(input("Geef een getal op:>"))

resultaat = (getal1 + getal2) * (getal1+getal2)

print(f"({getal1} + {getal2} ^2) = {resultaat}")