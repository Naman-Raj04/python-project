import math
history = []
while True:
    print("\n===Advanced calculator====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")
    print("5. power")
    print("6. square Root")
    print("7. view History")
    print("8. Exit")
    choice =input("Enter your choice(1-8):")
    if choice =="8":
        print("calculator closed!")
        break
    elif choice =="7":
        print("\ncalculator history:")
        for item in history:
            print(item)
        continue
    elif choice =="6":
        num = float(input("enter a number:"))
        result = math.sqrt(num)
        operation =f"√{num}={result}"
        print("Result:",result)
        history.append(operation)
    elif choice in["1","2","3","4","5"]:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        if choice == "1":
            result = num1+num2
            operation =f"{num1} + {num2}={result}"
        elif choice =="2":
            result = num1 - num2
            operation =f"{num1}-{num2}={result}"
        elif choice =="3":
            result = num1*num2
            operation = f"{num1}*{num2}={result}"
        elif choice =="4":
            if num2==0:
                print("Error! Division by zero.")
                continue
            result = num1/num2
            operation =f"{num1}/{num2}={result}"
        elif choice =="5":
            result = num1**num2
            operation = f"{num1}^{num2}={result}"
        print("Result:",result)
        history.append(operation)
    else:
        print("Indalid choice! please try again.")
