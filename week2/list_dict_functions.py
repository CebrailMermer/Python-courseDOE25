# ÖVNINGAR
#Listor
# -----
# Skapa lista med heltal och summera alla talen:
heltal=[1,2,3,4,5,6,7,8,9]
summa = sum(heltal)
print("Summan av heltal är: ", summa)
print()

# Största talet
Biggest_num = heltal[0]
for tal in heltal:
    if tal > Biggest_num:
        Biggest_num= tal
print ("Det största talet är: ", tal)
print()

# Mutiplikationstabeller
tal = int(input("Skriv in ett tal menllan 1 och 9 för att få multiplikationstabellen för det talet: "))
print(f"Multiplikationstabellen för {tal}: ")
for i in range (1,10):
    print(f"{tal} x {i} = {tal * i}")
    print()

# Filtrera jämna tal
tal_lista = list(range(1, 21))
for tal in tal_lista:
    if tal % 2 == 0:
        print (tal)
print()
# Vänd på en lista

lista = [1,2,3,4,5,6,7]
print("listan baklänges: ")
for i in range (len(lista)-1, -1, -1):
    print (lista[i])
    print()
# Dictionaries
# ------------
# Skapa en användarprofil
user = {
    "namn": "Anna",
    "age": 25,
    "stad":"Stockholm"
}
print("Användaaprofil: ",user)
print()
# Uppdatera profil med favoritfärg som användaren anger
favorite_color = input("Vad är din favoritfärg: ")
user["favorit color"]= favorite_color
print ("Uppdaterad användarprofil:", user)
print()
# Telefonbok
telefonbok = {
    "Anna": "0735554835",
    "Johan": "0705554488",
    "Kalle": "0739887722",
}

namn =input("Vem vill du slå upp i telefonboken: ")
if namn in telefonbok:
    print(f"{namn}s telefonnummer är: {telefonbok[namn]}")
else:
    print("Personen du söker finns inte i telefonboken: ")
    print()
# Ordrekvens
sentence =input("Skriv in en mening: ")
word_list = sentence.split()
word_freqvency = {}

for word in word_list:
    if word in word_freqvency:
        word_freqvency[word] +=1
    else:
        word_freqvency[word] = 1

print ("Ord och antal förekomster: ")
for word, frecvency in word_freqvency.items():
    print(f"{word}: {word_freqvency}")
    print()
# Inventarielista
        
    




