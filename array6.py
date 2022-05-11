from ast import Str


tamaño=0
array=[]
res=0


def pedirfrase():
    frase = str(input("Introduce el tamaño para el array: ")) 
    print(len(frase))
    print(frase)
    #print(frase[0])
    
    for letra in frase:
        array.append(letra)
        
    print(array)
    
if __name__=='__main__':
  pedirfrase()
  
   
          