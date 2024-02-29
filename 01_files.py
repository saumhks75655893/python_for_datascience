age = input("Enter your age : ")
print("Age : ", age)

f = open("age.txt", 'w')
f.write(age)

f.close()
