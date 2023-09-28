#oef7 

eerste_woord = input("Geef het eerste woord op:>")
tweede_woord = input("Geef het tweede woord op:>")

#controle   
# str.lower() --> zet om naar kleine letters
# str.upper() --> zet om naar hoofdletters

if str.lower(eerste_woord) == str.lower(tweede_woord):
    print("Deze twee woorden zijn exact gelijk.")
else:
    print("Deze woorden zijn verschillend.")

