#oef6 Vraag aan de gebruiker een aantal seconden op.
#Zet dit aantal om in dagen, uren, minuten en seconden.


#print(f"eerste versie: {getal/10}")     #--> reele deling (kommagetal)
#print(f"tweede versie: {getal//10}")    #--> gehele deling (deel voor de komma)
#print(f"derde versie: {getal%10}")      #--> de rest bij deling door een getal (modulo-operator)

totaal_aantal_seconden = int(input("Geef het aantal seconden op:>"))

#stap 1: hoeveel dagen zitten hier in?
aantal_dagen = totaal_aantal_seconden //(24*60*60)

#print(f"Het totaal aantal dagen is: {aantal_dagen}")

#hoeveel seconden zijn er nog over:
rest = totaal_aantal_seconden % (24*60*60)

#stap 2: hoeveel volle uren zit er in de rest?

aantal_uren = rest // (60*60)


#print(f"In de rest zitten nog volle uren: {aantal_uren}") 

#bepaal opnieuw de rest

rest = rest % (60*60)   #in programming, je leest van rechts naar links

# stap 3: hoeveel volle minuten zitten er in de rest?

aantal_minuten = rest // 60

#bepaal opnieuw de rest --> dat zijn de resterende seconden

aantal_seconden = rest % 60

print(f"d:h:m:s -> {aantal_dagen}:{aantal_uren}:{aantal_minuten}:{aantal_seconden}")