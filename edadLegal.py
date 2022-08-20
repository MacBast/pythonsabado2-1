#Entrada del problema
#Nivel del agua
edad=int(input("Digite su edad: "))

#proceso del problema
if(edad):
    if(edad>=0 and edad<14 ):
        print(f'De acuerdo a su {edad} años eres un Niño')
    elif(edad>=15 and edad<28):
        print(f'De acuerdo a su {edad} años eres un Joven')
    elif(edad>=29 and edad<60):
        print(f'De acuerdo a su {edad} años eres un adulto')
    elif(edad>=61 and edad<100):
        print(f'De acuerdo a su {edad} años eres un Adulto Mayor')
    elif(edad<0):
        print(f'De acuerdo a su {edad} Aun estas en la fabrica de papa')
    else:
        print("Eres Humano, no un alien")
else:
    print("digitaste una letra tarado")
