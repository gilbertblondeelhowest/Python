#oef4 
#Maak een Python programma dat de leeftijd van een hond vertaalt naar een overeenkomstige leeftijd
#van een mens.
#Vraag eerst aan de gebruiker de leeftijd van zijn hond. Nadien print je een correcte boodschap af
#waarbij:
#- Indien getal < 0, geef een foutmelding terug.
#- Indien leeftijd = 1 → 14 mensenjaren
#- Indien leeftijd = 2 → 22 mensenjaren
#- Indien meer dan 2: mensenleeftijd = 22 + (jaren – 2) * 5


leeftijd_hond = int(input("Geef de leeftijd van de hond op:>"))
if leeftijd_hond <= 0 :
    print("Foutmelding: geen geldige waarde!")
elif leeftijd_hond == 1:
    print("Deze leeftijd komt overeen met 14 mensenjaren")
elif leeftijd_hond == 2:
    print("Deze leeftijd komt overeen met 22 mensenjaren")
else:
    mensenleeftijd = 22 + (leeftijd_hond-2)*5
    print(f"Deze leeftijd komt overeen met {mensenleeftijd} mensenjaren")

