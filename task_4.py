#Program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers(using while loop)
total_sum = 0
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        break
    total_sum += number
print("The sum of all entered numbers is:", total_sum)

# Program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done"(using while loop)
while True:
    name = input("Enter a name : ")
    if name == "END":
        print("I am done.")
        break
    print(f"Name entered: {name}")
total_sum = 0

#Program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers(Using for loop)
for number in iter(lambda: float(input("Enter a number: ")), -1):
    if number < 0:
        break
    total_sum += number
print("The sum of all entered numbers is:", total_sum)

# Program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done"(using for loop)
for name in iter(lambda: input("Enter a name: "), "END"):
    if name == "END":
        print("I am done.")
        break
    print(f"Name entered: {name}")
