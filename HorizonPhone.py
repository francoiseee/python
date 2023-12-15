# Group Members: Ryna David, Francoise Gurango, Allein Dane Maninang, Justin Neri Pangilinan, Clarence Lane Parungao, Nikko Simeon Parungao, Chean Valencia

try:
    flag = False
    print("Welcome to Horizon Phone! We will recommend what plan's fit for you! Please answer the following: " )
    talk = int(input("Enter talk minutes needed: "))
    texts = int(input("Enter text messages needed: "))
    data = int(input("Enter gigabytes of data needed: "))

    if (talk < 0 or texts < 0 or data < 0) or (talk <= 0 and texts <= 0 and data <= 0):
        print("Invalid Input: You cannot enter all zeros or negative values")

    elif talk < 500 and data == 0: 
        flag = True
        if texts == 0:
            plan = "Plan A at $49 per month"
        else:
            plan = "Plan B at $55 per month"  
    
    elif talk >= 500 and data == 0:
        flag = True
        if texts < 100:
            plan = "Plan C at $61 per month"
        elif texts == 100:
            plan = "Plan C at $61 per month or Plan D at $70 per month"
        else:
            plan = "Plan D at $70 per month"
    
    elif data > 0:
        flag = True
        if data < 2:
            plan = "Plan E at $79 per month"
        elif data == 2:
            plan = "Plan E at $79 per month or Plan F at $87 per month"
        else:
            plan = "Plan F at $87 per month"
    
    print("We recommend this plan based on your current needs: \n" + plan)

except ValueError:
    print("Invalid Input: Please enter the correct values.")

except NameError:
    pass

else:
    if flag:
        print("We hope you find the best plan!")
finally:
    if flag:
        print("Thank you very much!")
    else:
        print("Invalid input, so no plan is recommended.")
