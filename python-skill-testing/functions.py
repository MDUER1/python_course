# function = A block of reusable code. Place () after the function name to invoke it

def happy_birthday():  # def foran funktionens navn, definerer den - og kalder den IKKE
    print("happy birth day")
    print("You are now older!")
    print("Hope you get many presents")


# Dette kører nu funktionen én gang. Lav funktioner små så de kan genbruges for gode vaner.
happy_birthday()

# Du kan putte data ind i paranteserne, altså funktionen kaldt argumenter når du kalder den.abs
# Det skal matche de parametere inde i funktionen som den er defineret.
# Så def happy_birthday(parameter), så kalder du den happy_birthday(argument)


def happy_birthday2(name):  # funktion med parametre
    print(f"happy birth day {name}")
    print(f"You are now older {name}!")
    print(f"Hope you get many presents{name}")


happy_birthday2("Marcus")

# Du kan altid tilføje flere argumenter i en funktion med komma imellem, så længere parametrene matcher
# Rækkefølgen er også vigtig

# return er en statement brugt i slutningen af en funktion, som sender et resultat tilbage til brugeren


def add(x, y):
    z = x + y
    return z


print(add(5, 5))

# Man kan se det som at funktionen bliver til hvad den returnerer. Her returneres z
# Da z = 10 så bliver funktionen når vi printer den 10, da det er hvad vi returnerer
