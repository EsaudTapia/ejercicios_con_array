from numpy import char


array=[]


def rellenar():      
    
    for n in range(65, 91):         
        chr_val = chr(n)           
        array.append(chr_val)
  

def buscar():
     
     indice=1
     
     while indice != -1:
       indice = int(input("Elija un indice entre 0 y 25, si quiere parar de consultar ingrese -1:  ")) 
       
       if indice == -1:
           print('Bye')
           break
       
       if indice <0 or indice >25:
           print ('error, es un numero menor o mayor al rango 0-25')       
       else:
          print(array[indice]) 
         

if __name__=='__main__':
     rellenar( )
     buscar()
     