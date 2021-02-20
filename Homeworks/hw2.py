# midterm, final , homework are grades
# stustens info name, surname 
# there are 5 students

"""  ## Asagidaki kod da kullanicadan alniyor ama ben hazir olsun diye ayrica ekledim  ## 

nameSurname = []
grades = []
for i in range(2):
    nameSurname.append(input("Ad Soyad giriniz :"))
    grades.append(list(map(int, input("3 not giriniz : ").split())))
        
"""
grades  = [[10,20,30,],[30,50,60],[70,10,100],[100,100,100],[80,90,70]]

nameSurname = ['Ali Erdem','Mehmet Uzun','Hasan Pak','Ayse Kisa','Fatma Demir']

studentDict = dict(zip(nameSurname, grades))

sorted_values = sorted(studentDict.values())

print("\nSorted Students list \n")

for i in sorted_values:
    for a,b in studentDict.items():
        if b == i:
            print(a,i)
            break
    
print("\nCongratulations {} you have the highest score in the class".format(a))
