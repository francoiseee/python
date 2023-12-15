# 1st example PRINT HELLO WORLD 5x
'''for i in range (5):
    print("Hello World1")'''


# (ending limit, , )
# (starting value, ending value, )
# (starting value, ending value, steps)


# 2nd example 1 TO 10
'''for number in range (1, 11):
    print(number)'''

# 3rd example BY 5
'''for number in range (5, 50, 5):
    print(number)'''

# 4th example BACKWARDS
'''for number in range (10, -1, -1):
    print(number)'''
    
# 5th exanple STRING ITERABLE
'''org = "LOOP"
for letter in org:
    print(letter)'''

# 6th example SUM OF 1 to n
'''total = 0
for num in range (1, 6):
    total += num

print(total)'''

# 7th example SUM OF 1 to n (inout values)
'''number = int(input("Enter a number: "))

total = 0
for num in range (1, number+1):
    total += num

print(total)'''

# 8th example PRINT VALUES 1 TO 10 BUT IT INCLUDES WHETHER OR NOT THAT NUMBER IS ODD OR EVEN
'''for n in range (1, 11):
    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")'''

# 9th example
# We need to make a program that iterates over a string and counts all of the vowels
# It should then output the number of vowels found in that string

'''string = input("Enter a string: ").upper()

total = 0

for letter in string:
    if letter == "A":
        total += 1
    elif letter == "E":
        total += 1
    elif letter == "I":
        total += 1
    elif letter == "O":
        total += 1
    elif letter == "U":
        total += 1

print(f"There are {total} vowels in {string}")'''

#ALPHABET PARTY BREAK

'''alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    print(letter)
    if letter == "Q":
        print("PARTY IS OVER!")
        break '''

#ALPHABET PARTY CONTINUE

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    if letter == "Q":
        continue
    print(letter)

# ALPHABET PARTY PASS
# PASS is a placeholder kapag hindi ka pa tapos sa code

'''alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    pass'''
