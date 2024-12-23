# LABORATORIO

# Tiempo estimado

# 5-10 minutos
# Nivel de dificultad

# Fácil
# Objetivos

# Familiarizar al estudiante con:

#     Utilizar la instrucción continue en los ciclos.
#     Modificar y actualizar el código existente.
#     Reflejar situaciones de la vida real en código de computadora.

# Escenario

# Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior (3.1.2.10) y crear un mejor devorador de vocales (bonito) mejorado! Escribe un programa que use:

#     Un ciclo for.
#     El concepto de ejecución condicional (if-elif-else ).
#     La declaración continue.

# Tu programa debe:

#     Pedir al usuario que ingrese una palabra.
#     Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
#     Usa la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
#     Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.

# Analiza el código en el editor. Hemos creado palabrasinVocal y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de ciclo, y asignarlo a la variable palabrasinVocal.

# Prueba tu programa con los datos que le proporcionamos.

# Datos de prueba

# Entrada de muestra: Gregory

# Salida esperada:
# GRGRY

# Entrada de muestra: abstemious

# Salida esperada:
# BSTMS

# Entrada de muestra: IOUEA

# Salida esperada:
 

palabraSinVocal = ""

userWord = input ("Ingresa tu palabra:")
userWord = userWord.upper ()

for letra in userWord:
	if letra == "A":
		continue
	elif letra == "E":
		continue
	elif letra == "I":
		continue
	elif letra == "O":
		continue
	elif letra == "U":
		continue
	else:
		palabraSinVocal += letra

print(palabraSinVocal)