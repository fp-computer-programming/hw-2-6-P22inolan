# Author: IBN (AMDG) 9/20/2021
free_throws = input("How many free throws were scored?")
two_points = input("How many two pointers were scored?")
three_points = input("How many three pointers were scored?")

score = (int(free_throws) + (int(two_points) * 2) + (int(three_points) * 3))

print("The player scored " + str(score) + " points in the game.")
