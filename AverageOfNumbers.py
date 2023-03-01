#Kathryn Tayar
#Completed Date:


#Description:
#Write a program named AverageOfNumbers.py that:

#(a) Asks the user for an integer (let us call this integer n), and
#(b)  Inputs n positive integers.
#(c)  Computes and prints the average of all the positive even integers and the average of all the positive odd integers. 
#   Negative values and zeros are ignored.
#(d) Displays each average as a floating point number to two decimal places along with an appropriate message. 
#   For example, if the user entered 9 for n and then entered 23 9 0 10 11 -9 22 6 7 13 18, the program would print a message such as:

               #You entered 4 even and 5 odd numbers.
               #The average of 10, 22, 6, 18 is: 14.00
               #The average of 23, 9, 11, 7, 13 is: 12.60
               #Have a great day!

#n = int(input("Enter the number of integers:"))



















#give users 3 tries to input n

tries = 0 
valid_int = False
even_count = 0
odd_count = 0
even_total = 0
odd_total = 0
evenlist = ""
oddlist = ""

while (tries < 3): 
        data = input("Enter the # of numbers you wish to enter: ")
        if(data.isdigit()): #valid integer
            valid_int = True
            break #
tries += 1
#if n is not valid print appropriate message
if(valid_int == False):
        print("Error: Input invalid, Goodbye.")

else: #input and process n integers
        #conver data to n
            n = int(data)
for i in range(1, n + 1):
        #ask for next number
        msg = "Enter integer #" + str(i) + ": "
        value = input(msg)
        if(value.isdigit()): # Valid int
            value = int(value) #converts to int
            if(value % 2 == 0): # value is even
                even_count += 1
                even_total += value
                if(evenlist == ""): 
                    evenlist = evenlist + str(value)

else:
             odd_count += 1
             odd_total += value
             oddlist += str(value)
             if(oddlist == ""): 
                    oddlist = oddlist + str(value)


print("You Entered", even_count, "even and", odd_count, "odd numbers.")
#evenResult = format(even_total/even_count, '.f2')
print("The average of", evenlist, "is:", even_total/even_count,)
#oddResult = format(odd_total/odd_count, '.f2')
print("The average of", oddlist, "is:", odd_total/odd_count,)
print("Have a Good Day!")