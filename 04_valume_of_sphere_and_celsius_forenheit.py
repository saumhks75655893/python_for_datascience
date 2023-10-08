# FIND THE VALUME OF THE SPHERE AND TAKE THE RADIUS OF THE SPHERE BY USER. 

radius = float(input("Enter the radius of the sphere : "))

# calculate the volume : -----

volume = round((4 / 3 * (3.14 * radius * radius * radius)), 3)

print(f"The volume of the sphere having the radius = {radius}  is {volume}")

# CELSIUS TO FORENHIET : ---------

# temperature taking in celcius : -----

celsius_temp = float(input("Enter the temperature in celsius : "))

# converting it into forenhiet : -----------

forenheit_value = (celsius_temp * 9/5) + 32

print("\n")
print("*"*60)
print(f"The temperature in celsius is = {celsius_temp} and \nafter converting in forenheit it is {forenheit_value}")
print("*"*60)