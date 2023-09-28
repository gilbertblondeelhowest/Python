# DEMO: gebruik default parameters in python
# DEMO: gebruik de parameternamen bij de functie-oproepe

def print_welkom(naam, voornaam, opleiding="MIT"):
    print(f"Welkom {voornaam} {naam} in Howest. Veel succes in {opleiding}!")


print_welkom(voornaam="Lies", opleiding="DAE", naam="Pinket")
print_welkom("Walcarius", "Stijn", "MCT")
print_welkom("Laprudence", "Christophe")