while True:		                                        #While Loop
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtrct' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'dived' to dived two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(":")
                                                        #If statements/Else statements/
    if user_input == "quit":                            #if expression:
        break                                           #   statements
    elif user_input == "add":                           #elif expression:
        num1 = float(input("Enter a number:"))          #   statements
        num2 = float(input("Enter another number:"))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number:"))          
        num2 = float(input("Enter another number:"))
        result = str(num1 - num2)
        print("The answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number:"))          
        num2 = float(input("Enter another number:"))
        result = str(num1 * num2)
        print("The answer is " + result)
    elif user_input == "dived":
        num1 = float(input("Enter a number:"))          
        num2 = float(input("Enter another number:"))
        result = str(num1 / num2)
        print("The answer is " + result)
    else:                                               #else:
       print("Unknown input")                           #   statements