
array=[]
 

def rellenar():
    for i in range (1,101):
        array.append(i)
    
    print (array)

def sumar ():
    suma=0
    for n in array:       
        suma+=n                
    print(f'la suma es {suma}')
    return suma
    

def promedio():
    
    suma= sumar()
    promedio= suma/100
    print(f'la promedio es {promedio}')
    


if __name__=='__main__':
  rellenar()

  promedio()
