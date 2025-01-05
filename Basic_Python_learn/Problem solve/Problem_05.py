# Traffic Light System
# Write a program that takes a color input (red, yellow, green) and prints the action:

# Red: Stop
# Yellow: Get Ready
# Green: Go

color=str(input("Enter color:-"))

if color=="red":
    print("Stop!!")
elif color=="yellow":
    print("Wait>>")
elif color=="green":
    print("Go")
else:
    print("Invalid color. Please enter red, yellow, or green.")