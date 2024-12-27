# BINARY FILES (IMAGE, VIDEOS, AUDIOS ETC.. )

f1 = open("green-hills.jpg",'rb')
f2 = open("green-hills_new.jpg",'wb')
b = f1.read()
f2.write(b)
print("A new image is available :  green-hills_new.jpg")
print()
''' Like this we can read or write any type of binary files like : videos, audios etc. '''

#  CSV FILE (COMMA SEPERATED VALUES ) 

import csv

# with open("students.csv",'w',newline="") as f: 
#     w = csv.writer(f)
#     w.writerow(['NAME','ROLLNO','MARKS','ADDRESS'])
#     while True: 
#         name = input("Enter the name of the student : ")
#         rollno = int(input("Enter the roll no. of the student : "))
#         marks = int(input("Enter the marks of the student : "))
#         addr = input("Enter the address of the student : ")
#         w.writerow([name, rollno, marks, addr])
#         option = input("Do you want to enter one more record [ yes / No ] : ")
#         if option.lower() == 'no':
#             break
        
# print('Total student data written successfully in csv file. ')

f = open("students.csv",'r')
r = csv.reader(f)
data = list(r)
print(data)

print()
print()

for row in data:
    print(row)

print()
print()
        
for row in data:
    for column in row:
        print(column, "\t",end="")
    print()