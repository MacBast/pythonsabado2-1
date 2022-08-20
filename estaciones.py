mes=(input("Digite el mes: "))

#proceso del problema
if(mes=="enero" or mes=="febrero" or mes=="marzo"):
    print(f'El mes {mes} es de Invierno')
elif(mes=="abril" or mes=="mayo" or mes=="junio"):
    print(f'El mes {mes} es de Primavera')
elif(mes=="julio" or mes=="agosto" or mes=="septiembre"):
    print(f'El mes {mes} es de verano')
elif(mes=="octubre" or mes=="noviembre" or mes=="diciembre"):
    print(f'El mes {mes} es de otono')
else:
    print("Digite una opcion valida")

