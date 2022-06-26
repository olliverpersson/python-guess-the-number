#Klicka på Run högst upp på skärmen för att testa programmet

#Berättar för datorn vilka funktioner vi behöver för programmet
import random

#Datorn väljer ett tal mellan 1 och 100, och sparar det i variabeln tal (variabler kan liknas med X i matte)
tal = random.randint(1,100)

#Skapar en variabel som heter gissning med värdet 0
gissning = 0

#Detta är en loop som låter oss fortsätta gissning tills vi har gissat rätt (alltså tills variabeln gissning är lika med variabeln tal)
while gissning is not tal:

  #Nu får användaren ange ett värde på variabeln gissning
  gissning = int( input("Gissa ett tal mellan 1 och 100: ") )

  #Om användaren gissade ett för litet värde så berättar vi det
  if gissning < tal:
    print("För litet")

  #Om användaren gissade ett för stort värde så berättar vi det
  if gissning > tal:
    print("För stort")

#Efter att loopen är färdig så berättar vi för användaren att de vann!
print("Du vann!")
print("Testa gärna att ändra i koden och testa vad som händer. Det är bästa sättet att lära sig programmering på!")