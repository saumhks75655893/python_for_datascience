# tell() - to return corrent position of the cursor from beginning of the file.

f = open("text1.txt",'r')
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(10))
print(f.tell())
print(f.read(2000))
print(f.tell())

print()
f.close()

# seek() - to move the cursur to one position to another

data = 'All students are stupid'
f = open('text1.txt','w')
f.write(data)
f.close()

with open('text1.txt','r+') as f:
    data = f.read()
    print(data)
    print("Current position of the cursor : ",f.tell())
    f.seek(17)
    print("Current position of the cursor : ",f.tell())
    f.write('Gems !!!')
    f.seek(0)
    text = f.read()
    print('Data after modification !!!')
    print("Current position of the cursor : ",f.tell())
    print(text)
    
print()   
#  WAP to check whether the given file is exists or not if exists then print its content. 

import os

fname = input("Enter the file name : ")
if( os.path.isfile(fname)):
    print("File exists : ",fname)
    f = open(fname,'r')
    print("The content of the file : \n\n")
    print(f.read())
else:
    print("File is not exists ",fname)

print()
#  WAP to print the number of lines , words and characters in the given file

fname = input("Enter the file name : ")
if( os.path.isfile(fname)):
    print("File exists : ",fname)
    f = open(fname,'r')
    lcount = 0
    wcount = 0
    ccount = 0

    for line in f: 
        lcount = lcount + 1
        words = line.split()
        wcount = wcount + len(words)
        ccount = ccount + len(line)
    
    print("The number of Lines : ",lcount)
    print("The number of Words : ",wcount)
    print("The number of characters : ",ccount)
    

    f.close()
else:
    print(f"The file \"{fname}\" is not exists in the system.")


    
    