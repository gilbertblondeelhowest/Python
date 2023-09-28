#oef4 Vraag aan de gebruiker de basis en de hoogte van een driehoek op.
#Bereken nadien de oppervlakte en print deze nadien af.

basis = float(input("Geef de basis van de driehoek op:>"))
hoogte = float(input("Geef de hoogte van de driehoek op:>"))

opp = basis * hoogte /2

print(f"De opp van de driehoek bedraagt {opp:.2f}")  # ":.2f" betekent 2 cijfers na de komma