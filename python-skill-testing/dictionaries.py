# Dictionaires er en collection af {key: value} par, og er ordered samt changeable. Men ingen duplikater

capitals = {"USA": "Washington D.C.",
            "Denmark": "København",
            "Sverige": "Stockholm",
            "India": "New Delhi"}

# For at få en værdi fra en dictionary, skriver du navnet på nøglen

print(capitals.get("Denmark"))

# Hvis du kalder en nøgle som ikke eksisterer, så retuneres None
# Du kan updatere eller udskifte et key-value par med -update, og hente med .get
# Du kan fjerne et key-value par med .pop og det seneste key-value par med .popItem
# .clear vil fjerne alt i dictionaryen
# .keys vil returnere alle nøglerne og .values vil retunere alle værdierne
# .items returnerer key-value parene i en 2D liste af tupler.
