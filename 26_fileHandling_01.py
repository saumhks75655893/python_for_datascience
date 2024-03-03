age = input("Enter your age : ")

# new file creating and adding some content 
f = open("age.txt", 'w')
f.write(age)
f.close()

f = open("age.txt", 'r')
print(f.read())
f.close()

# existing files opening 
f = open("text.txt", mode='r')
if f:
    print(f.read())
else:
    print("Some errors ! ")