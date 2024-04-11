# # tell() - to return corrent position of the cursor from beginning of the file.

# f = open("text.txt",'r')
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(10))
# print(f.tell())
# print(f.read(2000))
# print(f.tell())

# # seek() - to move the cursur to one position to another

# data = 'All students are stupid'
# f = open('text1.txt','w')
# f.write(data)

# with open('text1.txt','r+') as f:
#     data = f.read()
#     print(data)
#     print("Current position of the cursor : ",f.tell())
#     f.seek(17)
#     print("Current position of the cursor : ",f.tell())
#     f.write('Gems !!!')
#     f.seek(0)
#     text = f.read()
#     print('Data after modification !!!')
#     print("Current position of the cursor : ",f.tell())
#     print(text)
    
    
#  WAP to check whether the given file is exists or not if exists then print its content. 

import os

# fname = input("Enter the file name : ")
# if( os.path.isfile(fname)):
#     print("File exists : ",fname)
#     f = open(fname,'r')
#     print("The content of the file : \n\n")
#     print(f.read())
# else:
#     print("File is not exists ",fname)

#  WAP to print the number of lines , words and characters in the given file

fname = input("Enter the file name : ")
if( os.path.isfile(fname)):
    print("File exists : ",fname)
    