#Kathryn Tayar      Date: February 22, 2023
#Function 1:
def isLeapYear(year):
    
    #Returns True if the year is a leap year, and False otherwise.
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Function 2: takes a positive integer parameter as input, and computes and displays the smallest n such that n2 is greater than the integer entered
def greaterThanSquare(n):
     #Computes and displays the smallest integer n such that n^2 is greater than n.
     i = 1
     while i*i <= n:
        i += 1
        print("The square of", i, "is greater than", n, ".")
        print(i, "squared is:", i*i)


#Function 3: a string and a special character symbol.  The function adds the symbol before every character in the string except a space. 
# The function returns the new string with the symbol added
def addBefore(s, symbol):
    new_s = ''
    for c in s:
        if c == ' ':
            new_s += ' '
        else:
            new_s += symbol + c
    return new_s


#Function 4: takes two parameters: a string and a special character symbol.  The function adds the symbol after every character in the string except a space.
#  The function returns the new string with the symbol added.
def addAfter(s, sym):
    new_s = ''
    for c in s:
        if c == ' ':
            new_s += ' '
        else:
            new_s += c + sym 
    return new_s

#Function 5: takes an integer parameter as input and returns a list of squares of all integers between 1 and the number entered
def listOfSquares(n):
    squares = []
    for i in range(1, n+1):
        squares.append("(" + str(i) + "," + str(i*i) + ")")
    return ", ".join(squares)


#Function 6: takes two integer parameters as input and returns a list of squares of all integers between the first integer and the second integer.
def listOfSquaresMinMax(a, b):
    squares = []
    for i in range(a, b+1):
        squares.append("(" + str(i) + "," + str(i*i) + ")")
    return ", ".join(squares)



def main():
     a = int(input("Enter the first Integer: "))
     b = int(input("Enter the second Integer: "))
     minMax = listOfSquaresMinMax(a, b)
     print(minMax)
     
     n = int(input("Enter an Integer: "))
     squares = listOfSquares(n)
     print(squares)

     s = 'this is a test string'
     print(f"Original string:", s)
     print(f"Adding '-' after each character: {addAfter(s, '-')}")
     print(f"Adding '*' after each character: {addAfter(s, '*')}")
     print(f"Adding '123' after each character: {addAfter(s, '123')}")
     print(f"Adding '===' after each character: {addAfter(s, '===')}")

     s = 'this is a test string'
     print(f"Original string:", s)
     print(f"Adding '-' before each character: {addBefore(s, '-')}")
     print(f"Adding '*' before each character: {addBefore(s, '*')}")
     print(f"Adding '123' before each character: {addBefore(s, '123')}")
     print(f"Adding '===' before each character: {addBefore(s, '===')}")
     
     print()
     greaterThanSquare(9)
     greaterThanSquare(100)
     year = int(input("Enter a year: "))
     if isLeapYear(year):
        print(year, "is a leap year.")
     else:
         print(year, "is not a leap year.")



            






main()
