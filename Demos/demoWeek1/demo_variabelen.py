opleiding = input("Geef uw favoriete opleiding op: ")
geboortejaar = int(input("Geef uw geboortejaar op: "))

print(opleiding)
print(geboortejaar)

# uitvoeringsfout op volgende regel: op String geen rekenkundige bewerkingen mogelijk
geboortejaar = geboortejaar + 1
print(f"Het nieuwe geboortejaar is {geboortejaar}")

print(f"Datatype van de variabele opleiding is {type(opleiding)}")  # opleiding -> datatype: String!
print(f"Datatype van de variabele geboortejaar is { type(geboortejaar)}\n")  # geboortejaar -> datatype: String


# # datatypes: numeriek
getal1 = -12.25  # float
print(f"Datatype van de variabele getal1 is {type(getal1)} " )

getal2 = 3e+26J  # complex
print(f"Datatype van de variabele getal2 is {type(getal2)}")

# # multiple assignment
a = b = c = 10
a, b, c = 1, 2, "drie"
print(f"\nDatatype van de variabele c is {type(c)}")

# #delete commando
# del(a)          #variabele a bestaat niet meer
# #b = a          #compileerfout


# Ga naar demo_selectiestructuren.py