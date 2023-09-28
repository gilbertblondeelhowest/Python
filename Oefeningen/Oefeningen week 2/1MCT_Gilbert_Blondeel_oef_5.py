import math
#oef5 

#float zet de tekst om naar een komma getal
score = float(input("Geef een score op:>"))


#wat is het gedeelte na de komma?
#12.63--->0.63
#8.25---->0.25
decimal_part = score - int(score)
if decimal_part < 0.5:
    #we ronden af naar benede
    eind_score = math.floor(score)
else:
    #afronden naar boven
    eind_score = math.ceil(score)

    #controle
if eind_score >=10:
        print(f"U bent geslaagd met deze score:{eind_score}")
else:
          print(f"U bent niet geslaagd met deze score:{eind_score}")