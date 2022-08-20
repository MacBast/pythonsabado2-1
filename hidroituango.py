#Entrada del problema
#Nivel del agua
nivelAgua=int(input("Dijite el nuvel del agua de la presa de pollo: "))

#proceso del problema
if(nivelAgua>=0 and nivelAgua<20 ):
    print(f'El nivel de agua {nivelAgua} es muy bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'El nivel de agua {nivelAgua} es optimo')
elif(nivelAgua<=400):
    print(f'El nivel de agua {nivelAgua} es peligroso')
else:
    print("Digite una opcion valida")
