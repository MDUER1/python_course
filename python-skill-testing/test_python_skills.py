length1 = int(input("første sidelængde: "))
length2 = int(input("anden sidelængde: "))

# Beregn areal af firkant
areal = length1 * length2

print(f"Arealet af firkanten er {areal} i cm")

print("firkanten er stor") if areal > 10 else print("firkanten er lille")
