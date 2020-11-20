from art import logo

#Prints the ASCII art
print(logo)

def addition(n1, n2):
    """Takes two numbers and adds them together"""
    return n1 + n2

def subtraction(n1, n2):
    """Takes two numbers and subtracts the the second number from the first"""
    return n1 - n2

def multiplication(n1, n2):
    """Multiplies the two numbers together"""
    return n1 * n2

def division(n1, n2):
    """Divides the first number by the second number"""
    return n1 / n2

def exponent(n1, n2):
    """Raises the first number to the power of the second number"""
    return n1 ** n2

operations = {
     "+": addition,
     "-": subtraction,
     "*": multiplication,
     "/": division,
     "^": exponent,
}

calculating = True

num1 = float(input("what's the first number? "))
for symbol in operations:
    print(symbol)
operation = input("Pick an operation from above: ")
num2 = float(input("what's the second number? "))
solution = operations[operation](num1, num2)
print (f"{num1} {operation} {num2} = {solution}")

while calculating:
    response = input(f"Type 'y' to continue calculating with {solution} or type 'n' to exit: ")
    if response == "n":
        calculating = False
    elif response == "y":
        prevSolution = solution
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from above: ")
        nextNum = float(input("What's the next number? "))
        solution = operations[operation](solution, nextNum)
        print (f"{prevSolution} {operation} {nextNum} = {solution}")
    else:
        print("Please enter a valid response.")
