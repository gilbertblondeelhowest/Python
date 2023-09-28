# we voorzien elke functie van annotaties.
# Parameter Annotations


def bepaal_som(getal1: int, getal2: int, getal3: int):
    som = getal1 + getal2 + getal3
    return som


# print(f"Functie bepaalsom: {bepaal_som(44, 45, 2)}")

# Return Type Annotations
# def bepaal_som(getal1: int, getal2: int, getal3: int) -> int:
#     som = getal1 + getal2 + getal3
#     return som


# print(f"Functie bepaalsom: {bepaal_som(44, 45, 2)}")


def print_verwelkoming(naam: str, voornaam: str) -> None:
    print(f"{voornaam} {naam}, welkom in MCT!")
    print("Veel succes!")


print_verwelkoming("Walcarius", "Stijn")
                        