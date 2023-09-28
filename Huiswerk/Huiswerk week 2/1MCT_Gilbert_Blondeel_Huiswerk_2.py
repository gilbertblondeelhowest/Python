#thuis 2
#Schrijf een programma dat een kassasysteem nabootst.
#• Een broek kost 70,5 euro.
#• Een T-shirt kost 20,89 euro.
#• Een vest kost 100,3 euro.
#De gebruiker geeft per item het aantal gekochte goederen in. De computer berekent het te betalen
#bedrag.
#*** welkom bij het kassa systeem ***
#Hoeveel broeken werden er gekocht? 2
#Hoeveel T-shirts werden er gekocht? 3
#Hoeveel vesten werden er gekocht? 4
#Totaal te betalen:
#604.87

kostprijs_broek = 70.5
kostprijs_tshirt = 20.89
kostprijs_vest = 100.3
print(f"*** welkom bij het kassa systeem ***")

aantal_broeken = int(input("Hoeveel broeken werden er gekocht?"))
aantal_tshirts = int(input("Hoeveel T-shirts werden er gekocht?"))
aantal_vesten = int(input("Hoeveel vesten werden er gekocht?"))

totaal_broeken = kostprijs_broek*aantal_broeken
totaal_tshirts = kostprijs_tshirt*aantal_tshirts
totaal_vesten = kostprijs_vest*aantal_vesten


totaal_prijs = totaal_broeken+totaal_tshirts+totaal_vesten

print(f"{totaal_prijs}")


