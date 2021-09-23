# Author: IBN (AMDG) 9/23/2021

radius = input("What is your radius? ")
height = input("What is your height? ")

volume = (3.14) * (int(radius) ** 2) * int(height)
area = 2 * 3.14 * (int(radius) * (int(height) + int(radius)))

print("Your volume is: " + str(volume))
print("Your area is: " + str(area))
