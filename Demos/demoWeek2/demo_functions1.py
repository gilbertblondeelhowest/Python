# slecht voorbeeld herwerkt dmv functies
def beoordeel_getal(getal):
    if getal >= 200:
        print("Amai, da's een groot getal!")


def toon_som(getal1, getal2):
    som = getal1 + getal2
    print(f"Som: {som}")
    beoordeel_getal(som)


def toon_product(getal1, getal2):
    product = getal1 * getal2
    print(f"Product: {product}")
    beoordeel_getal(product)


getal_a = int(input("Geef het eerste getal op: "))
getal_b = int(input("Geef het tweede getal op: "))
toon_product(getal_a, getal_b)
toon_som(getal_a, getal_b)



