#  Program to input any character and check whether it is alphabet, digit or special character 
def charCheck(input_char): 
	if ((int(ord(input_char)) >= 65 and
		int(ord(input_char)) <= 90) or
		(int(ord(input_char)) >= 97 and
		int(ord(input_char)) <= 122)): 
		print( " Alphabet ")  
	elif (int(ord(input_char)) >= 48 and
			int(ord(input_char)) <= 57): 
		print(" Digit ")  
	else: 
		print(" Special Character ") 
input_char = '7'
charCheck(input_char)

#Program to input angles of a triangle and check whether triangle is valid or not
angle1 = float(input("Enter first angle of the triangle: "))
angle2 = float(input("Enter second angle of the triangle: "))
angle3 = float(input("Enter third angle of the triangle: "))

total = angle1 + angle2 + angle3

if total == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")

