# # DEMO:Een functie kan ook iets teruggeven


def bepaal_som(getal1, getal2, getal3):
    som = getal1 + getal2 + getal3
    return som


resultaat = bepaal_som(122, 123, 132)
print(f"De som van de drie getallen is {resultaat}")

# korter:
print(f"De som van de drie getallen is {bepaal_som(122, 123, 132)}")


# method overloading aanwezig in python?
# kan je twee methodes met dezelfde naam in python gebruiken?

# def bepaal_som(getal1, getal2, getal3) :
#     som = getal1 + getal2 + getal3
#     return som


# def bepaal_som(getal1, getal2, getal3, getal4) -> int:
#     return getal1 + getal2 + getal3 + getal4


# # Werken onderstaande regels?
# print(f"De som van de drie getallen is {bepaal_som(1, 1, 1)}")
# print(f"De som van de vier getallen is {bepaal_som(1, 1, 1, 5)}")
