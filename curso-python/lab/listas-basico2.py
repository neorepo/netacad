#  LABORATORIO

# Tiempo estimado

# 10-15 minutos
# Nivel de dificultad

# Fácil
# Objetivos

# Familiarizar al estudiante con:

#     Indexación de listas.
#     Utilizar operadoresin y not in.

# Escenario

# Imagina una lista: no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

# Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

# Nota: Asume que la lista original está ya dentro del código, no tienes que ingresarla desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.

# Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal, no necesitas actualizar la lista actual.

# No hemos proporcionado datos de prueba, ya que sería demasiado fácil. Puedes usar nuestro esqueleto en su lugar.

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista = []
for numero in miLista: # Explorar todos los números de la lista original.
    if numero not in nuevaLista: # Si el número no aparece en la nueva lista ...
        nuevaLista.append(numero) # ... adjúntalo aquí.
miLista = nuevaLista[:] # Hacer una copia de nuevalista.
print("La lista solo con elementos únicos: ")
print(miLista)