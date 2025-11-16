# nested loop = A loop within another loop (outer, inner)
# Her kommer nogle øvelser med nested-loops

# Print alle talpar til og med 1-3
for x in range(1, 4):
    for y in range(1, 4):
        print(x, y)

 # Print en firkant med tal
for row in range(1, 5):
    print(" ")
    for col in range(1, 6):
        print(row, end="")

print("")
print("")

# Print et pyramidemønster
for row1 in range(1, 6):
    for col1 in range(row1):
        print("*", end="")
    print()

# Multiplikationstabel fra 1-10
print()

for row2 in range(1, 11):
    print("")
    for col2 in range(1, 11):
        print(col2*row2, end=" ")
