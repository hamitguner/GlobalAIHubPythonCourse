# Date 16.02.2020
import random 

def isItPrime(x):  # Burada fonksiyonda sayinin asal olup olmadigi kontrol ediliyor.
    if x >1 :
        for i in range(2,x):
            if (x % i) == 0:
                return False
    else : # 0 dan kucukse sayi asal degildir.
        return False    
    
    return True        
    

# Bu program dinamik olarak calisir asagdaki satir ve stun boyutu degistirileblir.

rowSize = 3
colSize = 3
matrix = []

for i in range(rowSize):
    rows = []
    count = 0
    while count != colSize: # stun sayisi kadar asal sayi bulana kadar deniyor bu dongu.
        n = random.randint(0,100)
        if isItPrime(n): # Asal ise calisie
            rows.append(n) # Sayi asal ise satira ekle.
            count +=1
            
    matrix.append(rows) 
    
    
for i in matrix:
    print(i)    