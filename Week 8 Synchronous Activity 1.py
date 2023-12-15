try:
    ph_peso = float(input("Enter a value in Philippines Peso: P "))

    print ("Converstion Choices:")
    print ("Press: \n [A] for Phillipine peso to Japan Yen \n [B] for Philippine peso to US Dollar \n [C] for Philippine peso to UAE Dirham. ")

    enter = input("Enter your choice: ").lower()

    if enter == "a":
        peso = ph_peso / 0.50
        currency = "Japan Yen"
        symbol = "¥"
    elif enter == "b":
        peso = ph_peso / 52
        currency = "US Dollar"
        symbol = "$"
    elif enter == "c":
        peso = ph_peso / 14.50
        currency = "UAE Dirham"
        symbol = "د.إ"
    else:
        peso = 0

    print(f"{ph_peso} Philippine peso is equal to {symbol} {peso:.2f} {currency}")

except ValueError:
    print("Wrong Value!")
except NameError:
    print("Wrong input choice!")
finally:
    print("End of Program.")
