try:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        print("Please enter a positive number!")
    else:
        for i in range(num, 0, -1):
            for luh in range(i):
                print(i, end = "")
            print()
            
except ValueError:
    print("Please enter a positive number!")

