# Shopping-cart program til at øve lister, tuples og sets

# Tomme lister - benyttes fordi rækkefølgen vil beholdes
frugter = []
grøntsager = []
Total = 0
Priser = ()  # hurtigere + rækkefølge ligegyldig

while True:
    frugter = input("Hvilke frugter kunne du ønske dig? ")
    grøntsager = input("Hvilke grøntsager kunne du ønske dig? ")
    færdig = input("Er du færdig med din bestilling? (ja/nej) ")
    if færdig.lower() == "ja":
        break
    else:
        continue

print(frugter)
print(grøntsager)
