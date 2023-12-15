# Sample 1 
'''num = 0

while num <= 5:
    print (num)

    num = num + 1'''


# Sample 2

password = input("Enter a password: ")
validate_password = input("Enter a password again: ")

while password != validate_password:
    print("Passwords do not match!")
    validate_password = input("Enter a password again: ")

print("Your password was validated!")






