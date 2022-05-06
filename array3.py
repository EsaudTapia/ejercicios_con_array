import random

from sqlalchemy import false


tamaño=0
array=[]
res=0


def rellenar():
    tamaño = int(input("Introduce el tamaño para el array: ")) 
    print(len(array))
    while len(array) <= tamaño-1:
      # Ejecuta el bloque de código aquí
      # Siempre que el contador sea inferior a 10
        num = random.randint(1,70)  
        
        if esprimo(num):                   
          array.append(num) 
          
          
              
             
             
def esprimo(num):
     if num ==0 :
        return False
     if(num<2):
        return False
     if(num==1):
        return False
     
    
     for n in range(2, num):
        if num % n == 0:
            print("No es primo", num, "es divisor")
            return False
     print(f'Es primo {num}')
     
     return True
                                  
             
    
    
    


def mostrar():
    j=0
    for a in array :      
        print(f'en la posicion {j} esta: {a} '  )
        j+=1
        
def mayor ():
    ntemp=0
    
    for n in array:
        if n> ntemp:
            ntemp=n
        
    print(f'el numero mayo es {ntemp}')
    
    

if __name__=='__main__':
  rellenar()
  mostrar()
  mayor ()