import csv

# Abrimos el archivo CSV en modo lectura
with open('000ddb06-dcc8-4bbb-acb8-d457f9f715e1.csv', 'r') as file:
  # Creamos un lector CSV
  reader = csv.reader(file)
  
  # Iteramos sobre las filas del archivo
  for row in reader:
    # Accedemos a los valores de cada columna
    columna1 = row[0]
    columna2 = row[1]
    # ...
    
    # Imprimo valores de columna solo para Chequear qeu sí me muestra la Inormación
    print(columna1, columna2)