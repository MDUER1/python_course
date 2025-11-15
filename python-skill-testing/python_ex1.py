#Validate user input:

username = input("Skriv det brugernavn: ")

if len(username) < 12 and username.isalpha() == True:
    print("Du har skrevet dit brugernavn ind korrekt")
else:
    print("Du har ikke skrevet dig brugernavn ind korrekt")