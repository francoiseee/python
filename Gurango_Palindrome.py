# Gurango, Christine Francoise O.
# ICT - 104


while True:
    
    word = input("\nPlease enter a word (or type 'x' to end): ").casefold()
    w = ""
    
    for i in word:
        w = i + w

    if word == 'x':
        print("Thank you for using the program!")
        break
    
    if not word.isalpha():
        print("Please enter only letters!")
    else: 
        if (word == w):
            print("The entered word is palindrome!")
        else:
            print("The entered word is NOT palindrome!")
    
