import re
'''
+91 23 45 567 893
+92 34 45 679 100

Hello this is Himanshu kumar 
I'm a student. 
My phone numbers are: +1 555 123-4567, 0044 7987 654 3210, and 91 9876 543210.
'''

f1 = open('input1.txt','r')
f2 = open('output.txt','w')
for line in f1:
    print(line)
    ls = re.findall(r"\+?\d{1,4}\s?\d{2,4}\s?\d{2,6}[- ]?\d{2,4}", line)
    for number in ls: 
        f2.write(number+"\n")

f1.close()
f2.close()

print()
print()
f2 = open("output.txt",'r')
for line in f2:
    print(line)
f2.close()