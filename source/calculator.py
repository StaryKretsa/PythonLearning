import os
order = {"quit":0, "+":1, "-":2, "*":3, "/":4}              #dictionary
while True:		                                            #While Loop
    print("Options:")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(":")
                                                            #If statements/Else statements/
    if user_input not in order:                             #if expression:
        print("Unknown input")                              #   statements
    elif order[user_input] == 0:                            #elif expression:  
        break                                               #   statements
    else:                                                   #else:
        while True:                                         #   statements
            result = ""                                        
            try:                                            #Exception Handling 
                num1 = float(input("Enter a number:"))
                num2 = float(input("Enter another number:"))
                if order[user_input] == 1:                             
                    result = str(num1 + num2)                                       
                elif order[user_input] == 2:              
                    result = str(num1 - num2)               
                elif order[user_input] == 3:
                    result = str(num1 * num2)
                elif order[user_input] == 4:
                    result = str(num1 / num2)                                    
            except Exception as e:
                print("An Error occurred:")
                print(str(e))
                pr int("#######################")
                print("Please enter the numbers again.")
                os.system("PAUSE")
            else:
                print("The answer is " + result)
                os.system("PAUSE")
                break
            finally:
                os.system("cls")
