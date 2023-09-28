# DEMO: scope van variabelen
# lokale variabele
def test_methode1():
    #gebruik van een lokale variabele
    naam_hogeschool = "Howest"
    print(f"De naam van de school is {naam_hogeschool}")

test_methode1()
print(naam_hogeschool)     # <--- Foutmelding: waarom?



# globale variabele
naam_hogeschool = "Vives"

def test_methode2():
    #gebruik van een lokale variabele
    jaartal = 2020
    #TEST 1
    #naam_hogeschool = "Howest"
    #TEST 2: wat doet global?
    # global naam_hogeschool  ------> we maken gebruik van de globale var
    naam_hogeschool = "Howest"
    print(f"In de test-methode2: De naam van de school in {jaartal} is {naam_hogeschool}")


test_methode2()
print(f"Buiten: De naam van de school is {naam_hogeschool}")

