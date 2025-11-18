texto = "Hola Mundo"
print(texto.upper())
print(texto.lower())
print(texto.find("M"))
print(texto.find("Mun"))
print(texto.find("mun"))
nuevotexto = texto.replace("Mun", "buenas")
print(texto, nuevotexto)
print("Mundo" in texto)