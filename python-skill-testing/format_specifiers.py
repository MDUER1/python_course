#format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 234.21
price2 = 3242.234224
price3 = 312

print(f"Din pris er {price1:.3f}") #Her er .3f en tre decimaler float konverter flag
print(f"Din pris er  {price2:10}") #Her er 10 blot 10 mellemrum før prisen
print(f"Din pris er {price3:010}") #Her bliver der tilføjet 0'er foran prisen til dens string er 10 karakterer

print(f"Din pris er {price1:<10}") #her bliver dine tal aligned til venstre med 10
print(f"Din pris er {price2:<10}") 
print(f"Din pris er {price3:<10}")

print(f"Din pris er {price1:>10}") #her bliver dine tal aligned til højre med 10
print(f"Din pris er {price2:>10}") 
print(f"Din pris er {price3:>10}")

print(f"Din pris er {price1:^10}") #her bliver dine tal centreret med 10
print(f"Din pris er {price2:^10}") 
print(f"Din pris er {price3:^10}")

print(f"Din pris er {price3:+}") # sætter et positivt +-tegn foran tal og negative tal forbliver negative
print(f"Din pris er {price2:,}") # separerer hvert tusinde med et komma for overskulighed

#Du kan kombinerer flags
print(f"Din pris er {price1:^10,.5f}")
print(f"Din pris er {price2:^10,.5f}")
print(f"Din pris er {price3:^10,.5f}")