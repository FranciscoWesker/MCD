def mcd(a, b):
 resto = 0       
 iteracion = 1
 while(b > 0):
   resto = b
   b = a % b
   a = resto
   print("Residuo de iteración ", iteracion, ": ", b)
   iteracion+=1
 return iteracion    
numeroMayor = int(input("Introduce el número mayor de la pareja a la cual desea calcular el MCD: "))

numeroMenor = int(input("Introduce el número menor de la pareja a la cual desea calcular el MCD: "))    
print("El máximo común divisor de ", numeroMayor," y ", numeroMenor," es ", mcd(numeroMayor, numeroMenor))
