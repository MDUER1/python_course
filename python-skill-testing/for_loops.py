# for loops = eksekverer en blok kode et bestemt antal gange. Du kan itererer over en range, string squence osv.

# x er en counter som tæller og range inkluderer startpunkt og ekskluderer slutpunkt
for x in range(1, 11):
    print(x)

# Tæller baglens fra 10 til 1 og printer "godt nytår" til sidst
for x in reversed(range(1, 11)):
    print(x)

print("GODT NYTÅR!")

# Du kan også benytte steps i range, da den går range(start, slut, spring)
for x in reversed(range(1, 11, 2)):  # spring baglens med 2 fra 11 til 1
    print(x)

# Du kan også itererer over strings
kredit_kort = "1321-1231-2134"

for x in kredit_kort:  # skriver alle tallene ud på en række
    print(x)

for x in reversed(kredit_kort):  # skriver alle tallene ud på en række balgens
    print(x)

# Du kan benytte "continue" til at spole over en iteration

for x in range(1, 21):  # Itererer 1 - 20
    if x == 13:
        continue  # springer 13 over
    else:
        print(x)  # printer hver iteration x antager

# Du kan benytte "break" til at brække dig selv ud af loopet

for x in reversed(range(1, 11)):  # tæller ned fra 10
    if x == 5:
        break  # stopper nedtælling ved 5
    else:
        print(x)  # printer nedtælling
