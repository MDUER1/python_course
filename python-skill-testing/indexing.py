# Tester indexing skills
# [start (inklusiv): end(eksklusiv); step]

# variabel
kredit_kort = "1732-4929-3473"

# Bestem de første 4 tal
# for at få alt fra start til slutpunkt, lad førstekoordinat stå tomt eller lig 0
print(kredit_kort[:4])

# Bestem det andet sæt 4 tal
print(kredit_kort[5:9])

# Bestem det sidste sæt tal af 4
# lad slut være tom for at få alle karakterer fra startpunkt til slutpunkt
print(kredit_kort[10:])

# Benyt negativ-indeksering til at få de sidste tal i din string
print(kredit_kort[-1])  # sidste tal
print(kredit_kort[-2])  # andet siste tal
print(kredit_kort[-4:])  # sidste fire tal

# Spring i tallene vha. steps
print(kredit_kort[::2])  # tæller hver-anden fra start til slut
print(kredit_kort[::3])  # tæller hver-tredje
# få hverandet sidste tal vha. negativ indexing + steps
print(kredit_kort[-4::2])
print(kredit_kort[:4:2])  # få hverandet tal i de første 4
print(kredit_kort[::-1])  # negative steps vender om på rækkefølgen i en string
print(kredit_kort[:-5:-1])  # vend de sidste 4 karakterer
