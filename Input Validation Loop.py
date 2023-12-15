# Input Validation Loop

'''
valid_input = False

while not valid_input:
    try:
        user_age = int(input("Enter your age: "))
        valid_input = True
    except ValueError:
        print("Invalid input. Please enter a value integer.")

print("Your age is:", user_age)
'''

'''
valid_input = ["YES", "NO"]
answer = input("Yes or No: ").upper()

while answer not in valid_input:
    print("Invalid input. Please try again!")
    answer = input("Yes or No: ").upper()

print("Thanks")
'''

text = input("Enter a message: ")

print("How do you want to format your text:")
print("[1] Uppercase")
print("[2] Lowercase")
print("[3] None")

valid_input = [1, 2, 3]

choice = int(input("Choice: "))

while choice not in valid_input:
    print("Invalid input. Try again!")
    choice = int(input("Choice: "))

if choice == 1:
    print(text.upper())
elif choice == 2:
    print(text.lower())
else:
    print(text)
