# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates Ok. Faster
# List, Set og Tuple går under betegnelsen "collection"
# hvert element i en collection er en værdi

fruits = ["apple", "banana", "orange", "kiwi", "coconut"]  # liste

print(fruits[1])  # printer element 1 (banan), da indekser starter i element 0
# printer alle elementer, hvor startpunkt er inkluderende og slutpunkt er ekskluderende
print(fruits[0:3])
# printer hvert andet element da indekseringer er [start;slut:spring]
print(fruits[:5:2])
# printer indekset i omvendt rækkefølge da negative spring er modsat retning
print(fruits[::-1])

# Du kan itererer over collections + mange flere funktioner:

for fruit in fruits:  # printer frugterne i listen
    print(fruit)

# Du kan benytte "in" operatoren for at se om et element er i en collection, som returnerer en bool-value
print("apple" in fruits)

# Du kan reassign nye værdier til specifikke elementer i lister
fruits[1] = "pineapple"

# Du kan også tilføje elementer til en liste ved append
fruits.append("pineapple")

# Du kan fjerne et element gennem remove
fruits.remove("apple")

# Du kan insert elementer i en liste gennem .insert til en bestemt plads
fruits.insert("pineapple")

# Du kan også sorterer en liste alphabetisk med .sort
fruits.sort

# Du kan reverse en liste med reverse
fruits.reverse()

# For at clear/slette alle elementer i en liste benyt .clear
fruits.clear()

# Du kan bestemme nummeret/indekset af et element gennem .Index
print(fruits.index("apple"))

# Du kan også tælle antallet af elementer i en liste
fruits.count("banana")

# Du kan også arbejde med det som hedder "sets", hvilket blot er skrives som lister hvor [] er {}

# unordered - så ingen bestem rækkefølge, ændres hver gang
biler = {"porsche", "mercedes", "audi", "opel"}

# Du kan heller ikke have duplikater i et set.

# Tupler er hurtigere end lister, og kan også havde duplikater, men er unchangeable, [] = ()

elektronik = ("keyboard", "mus", "skærm", "tast", "tv")

# Dvs tuples og sets kan ikke ændres så snart de er lavet, men det kan lister

# Lister benyttes hvis du skal have evnen til at ændre dens indhold undervejs,
# eller hvis rækkefølgen er vigtig, eller hvis det samme element kan gå igen

# Du benytter tuples når dataen i den ikke skal ændres og er fastlåst
# Tuples kan også benyttes som keys i dictionaries
# Tuples har bedre ydeevner så benyt dem hvis muligt over lister

# benyt sets hvis rækkefølgen er ligegyldig og der ikke må optræde dubletter
# så fx når du gerne automatisk vil fjerne en dublet
# Eller til hurtige opslag samt mængdeoperationer
