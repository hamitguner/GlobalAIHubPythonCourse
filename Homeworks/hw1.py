import random 

# Bu program dinamik olarak calisir asagdaki satir ve stun boyutu degistirileblir.

rowSize = 3
colSize = 3
matrix = []

for i in range(rowSize):
    rows = []
    count = 0
    while count != colSize: # stun sayisi kadar asal sayi bulana kadar deniyor bu dongu.
        n = random.randint(0,100)
        if n > 1 :
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else:
                rows.append(n) # Sayi asal ise satira ekle.
                count +=1
            
    matrix.append(rows) 
    
    
for i in matrix:
    print(i)    
    