
# f = open("age.txt", 'r')
# print(f.read())
# f.close()

# # existing files opening 
# f = open("text.txt", mode='r')
# if f:
#     print(f.read())
# else:
#     print("Some errors ! ")     
    
# print("Name of the file : " , f.name)
# print("Mode : ",f.mode)
# print("is closed : " , f.closed)
# print("Is readable : " ,f.readable())
# print("Is writable : ",f.writable())

# f.close()


# # writting the data 
# f = open("text.txt",'w')
# f.write("Himanshu kumar \n")
# f.write("Sundaram kumar \n")


# a =['Hey ! \n', 'What are you doing?\n',"I'm going to market, whould you go with me?\n"]
# f.writelines(a)
# print("Content written successfully ! ")
# f.close()

# #  reading data 
# print()
# print()
# print()
# f = open("text.txt",'r')
# print(f.read())
# # print()
# # print()
# # print(f.read(10))
# # print()
# # print()
# # print(f.readline())
# # print()
# # print()
# # lines = f.readlines()
# # for line in lines: 
# #     print(line , end='')

# f.close()

with open('text.txt','r') as f:
    print(f.read())
    print("is closed : ",f.closed)
    
print("is closed : ",f.closed)
