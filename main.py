import re
path = "Ejemplo.txt"
try:
    archivo = open(path, 'r')
except:
    print ("Archivo no encontrado")
    quit()
texto = ""
for linea in archivo:
    texto += linea
print("El archivo txt contiene:")
print("------------------------------------------------------------------")
print (texto)
print("------------------------------------------------------------------")
print("")
print("\n")
#Busca y muestra variables validas
PatronVV = r"[a-zA-Z$_][a-zA-Z0-9$_]*"
ResultadoVV = re.findall(PatronVV,texto)
print("*******************************************************************")
print ("Resultado de la búsqueda de las variables validas")
print("*******************************************************************")
print(ResultadoVV)
print("\n")
#Busca y muestra enteros y decimales
PatronED = r"\d+\.?\d*"
ResultadoED = re.findall(PatronED,texto)
print("*******************************************************************")
print ("Resultado de la búsqueda de enteros y decimales")
print("*******************************************************************")
print(ResultadoED)
print("\n")
#Busca y muestra expresiones aritmeticas
PatronEA = r"(\w*(?:\s[(\+|\-|\*|\\)*]\s\w*)+)"
ResultadoEA = re.findall(PatronEA,texto)
print("*******************************************************************")
print ("Resultado de la búsqueda de las expresiones aritmeticas")
print("*******************************************************************")
print(ResultadoEA)
print("\n")
#Busca y muestra operadores condicionales
PatronOC = r"(\w*(?:\s[(\>|\<|\=|\!)*]\s\w*)+)"
ResultadoOC = re.findall(PatronOC,texto)
print("*******************************************************************")
print ("Resultado de la búsqueda los operadores condicionales")
print("*******************************************************************")
print(ResultadoOC)
print("\n")
#Busca y muestra cadena de caracteres
PatronCC = r"[(\w|\W)*]*"
ResultadoCC = re.findall(PatronCC,texto)
print("*******************************************************************")
print ("Resultado de la búsqueda de la cadena de caracteres ")
print("*******************************************************************")
print(ResultadoCC)
