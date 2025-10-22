print("command line basic arithmetic calculator")
print("What kind of operation would you like to do?")
print("+, -, *, /, ^")

#definition of the operationchoice function

def operationchoice():

    #number input
    x = (float(input("Enter your first number: ")))
    y = (float(input("Enter your second number: ")))
    operation = input("Type the operation you want to perform: ")

    #Checks wich operation

    if operation == "+":
        print(float(x + y))

    if operation == "-":
        print(float(x - y))

    if operation == "*":
        print('\n')
        print(float(x * y))

    if operation == "/":
        #Checks if your dividing by zero to avoid returning an error
        if y == int(0):
            print('\n')
            print("You cannot divide by zero")
        else:
            print('\n')
            print(float(x / y))
    if operation == "^":
        print('\n')
        print(float(x ** y))


operationchoice()





