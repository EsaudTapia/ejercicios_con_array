import random


tamaño=0
array=[]


def rellenar():
    tamaño = int(input("Introduce el tamaño para el array: ")) 
    
    for i in range(tamaño):
        num = random.randint(0,9)        
        array.append(num)
    
    
    print(array)


def mostrar():
    j=0
    for a in array :      
        print(f'en la posicion {j} esta: {a} '  )
        j+=1
if __name__=='__main__':
  rellenar()
  mostrar()