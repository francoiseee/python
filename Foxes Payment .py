try: 
    name = input("Enter your name: ")
    print("Code     Payment Service Option \n CI     Cash In \n CO     Cash Out")
    service = input("Enter the payment service option code: ").lower()
    money = float(input("Enter the money you want to cash in/out (PhP): "))
    print('-' * 50)
    print("\t \t Foxes Payment")
    print('-' * 50)

    match service: 
        case 'ci':
            p = "Cash In"
            if money >= 0.01 and money <= 9999.99:
                fee = 0
                total = (money + 0)
                US = (total / 55)
            if money >= 10000:
                fee = (money * 0.02)
                total = (money + fee)
                US = (total / 55)

        case 'co':
            p = "Cash Out"
            if money >= 0.01 and money <= 9999.99:
                fee = 10
                total = (money - 10)
                US = (total / 55)
            if money >= 10000 and money <= 19999.99:
                fee = 15
                total = (money - 15)
                US = (total / 55)
            if money >= 20000 and money <= 49999.99:
                fee = 20
                total = (money - 20)
                US = (total / 55)
            if money >= 50000:
                fee = 25
                total = (money - 25)
                US = (total / 55)
        case _:
            fee = 0
            total = 0
            US = (total / 55)
            print(f"Payment Service Selected\t None")
            print(f"Amount of Money Php {money:,.2f}")
            print(" ")
            print(f"Service Fee Php {fee} \n TOTAL BILL Php {total:,.2f}")
            print (" ")
            print (f"US DOLLAR AMOUNT $ {US:,.2f}")
            
            
    print(f"Payment Service Selected {p}")
    print(f"Amount of Money Php {money:,.2f}")
    print(" ")
    print(f"Service Fee Php {fee} \n TOTAL BILL Php {total:,.2f}")
    print (" ")
    print (f"US DOLLAR AMOUNT $ {US:,.2f}")
    print('-' * 50)
    print("Thank you for availing of our service! \n Have a nice day Foxes!")
    print('-' * 50)
    
except TypeError:
    print("ERROR: Please enter a valid data input.")
except NameError:
    print("ERROR: Please enter a valid transaction code.")
except ValueError:
    print("ERROR: Please enter a valid data input")
