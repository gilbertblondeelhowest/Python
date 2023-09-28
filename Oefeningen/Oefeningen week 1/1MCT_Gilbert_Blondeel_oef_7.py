#oef7 Vraag aan de gebruiker een int-getal n op. Bereken de volgende som: n + nn + nnn.
#Print het resultaat af.

# 3 ----> 3 + 33 +333
# 5 ----> 5 + 55 +555
cijfer = int(input("Geef een cijfer op:>"))
resultaat = cijfer + cijfer*11 + cijfer*111

print(f"Het resultaat is {resultaat}")

#versie 2 (alternatief)

cijfer = input("geen een getal op:>")
resultaat = int(cijfer) + int(cijfer+cijfer) + int(cijfer+cijfer+cijfer)

print(f"Het resultaat is {resultaat}")

