# FIND THE VALUME OF THE SPHERE AND TAKE THE RADIUS OF THE SPHERE BY USER. 

radius = float(input("Enter the radius of the sphere : "))

# calculate the volume : -----

volume = round((4 / 3 * (3.14 * radius * radius * radius)), 3)

print(f"The volume of the sphere having the radius = {radius}  is {volume}")