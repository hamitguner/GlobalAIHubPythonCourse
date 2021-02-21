# homework 3 

first500 = []
last500 = []

def prime_first(number):
    global first500 
    if number > 1 :
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            first500.append(number)
            
    if number == 499:
        print("0 500 arasi asal olan sayilar \n")
        print(first500)



def prime_second(number):
    global last500 
    if number > 1 :
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            last500.append(number)
            
    if number == 999:
        print("\n500 100 arasi asal olan sayilar \n")
        print(last500)        
        

for i in range(0,1000):
    if i < 500:
        prime_first(i) 
    else:
        prime_second(i)