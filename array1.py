
numero=0
array=[]


def rellenar():
   for i in range(10):
      numero = int(input("Introduce un numero: ")) 
      array.append(numero)

def mostrar():
    print('numeros del array')
    for num in array:
        print(num)


if __name__=='__main__':
    rellenar()
    mostrar()