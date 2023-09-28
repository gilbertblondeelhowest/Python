#thuis 3
#Pas de uitvoer als volgt aan (let op het inspringen en de spaties):
#*** welkom bij het kassa systeem ***
#Hoeveel broeken werden er gekocht? 2
#Hoeveel T-shirts werden er gekocht? 3
#Hoeveel vesten werden er gekocht? 4
#U kocht:
#Broeken: 2 stuk(s)
#T-Shirts: 3 stuk(s)
#Vesten: 4 stuk(s)
#Totaal:604.87

kostprijs_broek = 70.5
kostprijs_tshirt = 20.89
kostprijs_vest = 100.3
print(f"*** welkom bij het kassa systeem ***")

aantal_broeken = int(input("Hoeveel broeken werden er gekocht?"))
aantal_tshirts = int(input("Hoeveel T-shirts werden er gekocht?"))
aantal_vesten = int(input("Hoeveel vesten werden er gekocht?"))

print(f"U kocht:\n\tBroeken:{aantal_broeken} stuck(s)\n\tT-shirts: {aantal_tshirts} stuck(s)\n\tVesten:{aantal_vesten} stuck(s)")

totaal_broeken = kostprijs_broek*aantal_broeken
totaal_tshirts = kostprijs_tshirt*aantal_tshirts
totaal_vesten = kostprijs_vest*aantal_vesten


totaal_prijs = totaal_broeken+totaal_tshirts+totaal_vesten

print(f"Totaal:{totaal_prijs}")



