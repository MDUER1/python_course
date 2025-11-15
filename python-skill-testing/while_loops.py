# While loops er et loop som ekseverer kode imens (while) en condition/krav forbliver sand

# Eksempel, gentager "skriv dit navn" indtil det krav opfyldes hvor koden så eksekverer videre til print.
import math
name = input("Skriv dit navn: ")

while name == "":
    # Husk en måde at slippe ud af loopet, så det ikke blive infinit
    name = input("Skriv dit navn: ")

print(f"Hej {name}")

# Eksempel
age = int(input("Hvor gammel er du: "))

while age < 0:
    print("Fejl")
    age = int(input("Skriv igen hvor gammel du er: "))

print(f"hej {name}, du er {age} år gammel")

# Eksempel hvor vi beregner renter med et while-loop:


# variabler
final_amount = 0
initial_balance = 0
interest_rate = 0
periods_elapsed = 0
times_of_compounded_interest_per_year = 0

# Funktionen
while initial_balance <= 0:
    initial_balance = float(input("Enter your initial balance: "))
    if initial_balance <= 0:
        print("Din balance kan ikke være 0 eller negativ, indtast en ny")

while interest_rate == 0:
    interest_rate = float(input("Enter your interest rate: "))

while periods_elapsed <= 0:
    periods_elapsed = float(input("Enter periods elapsed: "))
    if periods_elapsed <= 0:
        print("Perioden som er gået kan ikke være 0 eller negativ, indtast en ny")

while times_of_compounded_interest_per_year <= 0:
    times_of_compounded_interest_per_year = float(
        input("Enter compound interest per year: "))
    if times_of_compounded_interest_per_year <= 0:
        print("Perioden kan ikke være 0 eller negativ, indtast en ny.")

final_amount = initial_balance*(1 + interest_rate/(times_of_compounded_interest_per_year)
                                )**(times_of_compounded_interest_per_year*periods_elapsed)

print(f"Hej {name} du er {age}, og vil have en slutmængde på {final_amount}")
