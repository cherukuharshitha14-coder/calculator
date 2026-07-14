# Main Program
while True:
    print("\n******** CALCULATOR ********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", addition(a, b))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", subtraction(a, b))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", multiplication(a, b))

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", division(a, b))

    elif choice == 5:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        print("Result =", modulus(a, b))

    elif choice == 6:
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result =", power(a, b))

    elif choice == 7:
        a = float(input("Enter a number: "))
        print("Result =", square(a))

    elif choice == 8:
        a = float(input("Enter a number: "))
        print("Result =", square_root(a))

    elif choice == 9:
        n = int(input("Enter a non-negative integer: "))
        print("Result =", factorial(n))

    elif choice == 10:
        print("Exiting Calculator...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 10.")
        
