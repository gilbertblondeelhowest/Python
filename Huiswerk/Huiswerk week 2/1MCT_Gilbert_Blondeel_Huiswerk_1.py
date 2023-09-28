#thuis 1 
#Om de prijs van een woning te bepalen, telt men de prijs van de bouwgrond en de eigenlijke bouw op.
#Het btw-tarief op dit totaal is 21 %.
#Je vraagt aan de gebruiker de prijs van de bouwgrond en de prijs van het gebouw.
#Je toont het totaal te betalen bedrag.
#Prijs van de bouwgrond? 125000
#Prijs van het gebouw? 180000
#De totale kostprijs van het project is: 369050.0
#Zorg dat de invoer ook een kommagetal mag zijn.
#Prijs van de bouwgrond? 125000.5
#Prijs van het gebouw? 190000.9
#De totale kostprijs van het project is: 381151.694

prijs_bouwgrond = float(input("Prijs van de bouwgrond?"))  
prijs_gebouw = float(input("Prijs van het gebouw?")) 
total_met_btw = (prijs_bouwgrond + prijs_gebouw) *1.21

print(f"de totale kostprijs van het project is:{total_met_btw}")



