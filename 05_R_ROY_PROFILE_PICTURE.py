'''  
Q.2 ->  Roy want to change his profile picture on Facebook. Now Facebook has some restrictions over the dimension of picture that we can upload. Minimum dimension fo the picture can be LxL, where L is the length of the side of square. 

Now Roy has N photos of various dimensions.
Dimension of a photo is denoted as W x H. 
where W - width of the photo and H - height of the photo.
When any photo is uploaded following events may occur.

1. If any of the width or height is less than L, user is pramoted to upload another one. Print "UPLOAD ANOTHER" in this case.
2. If width and height, both are larger enough and 
    a.  If the photo is already square then it is accepted. Print "ACCEPTED" in this case. 
    b. Else user is promted to crop it. Print "CROP IT" in this case. (quotes are only for clarification)

Given, L,N,W and H as input, print appropriate text as output.     
'''

L = int(input("Enter the value : "))
N = int(input("Enter the Number of Photos : "))


for i in range(N):
    W = int(input("Enter the value : "))
    H = int(input("Enter the value : "))

    if W < L or H < L:
        print("UPLOAD ANOTHER.....")
    elif W >= L or H >= L:
        if (W == L) and (H == L):
            print("ACCEPTED....")
        else:
            print("CROP IT .... ")
