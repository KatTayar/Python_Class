#Develop and test a Python program called ArithmeticOperators that that reads two values from the keyboard, applies the arithmetic operators, one at a time,
#and prints the result after each operator is applied. For example, if the two values read from the keyboard are 6 and 9, then the program would output the following:
#Showing results of applying the arithmetic operators: +, -, *, /, //, %, **

       



 
#Note that you will need to use the format function for lines 4 and 7.

#get 1st value
a = input("Enter first value: ")
#num1 = float(a)
num1 = int(a)
b = input("Enter first value: ")
#num2 = float(b)
num2 = int(b)

# 6 + 9 = 15
print(num1, "+",num2,"=",num1+num2)

#6 - 9 = -3
print(num1, "-",num2,"=",num1-num2)

#6 * 9 = 54
print(num1, "*",num2,"=",num1*num2)

#6 / 9 = '0.67'
#print(num1, "/",num2,"=",num1/num2)

#txt1 = "6 / 9 = {0:.2f}"
#Equal = (num1/num2)
#print ("6/9 = {number, 0:.2f}".format(Equal))

txt1 = "6 / 9 = {:.2f}"
print(txt1.format(num1/num2))
 

#6 // 9 = 0
print(num1, "//",num2,"=",num1//num2)

#6 % 9 = 6
print(num1, "%",num2,"=",num1%num2)

#6 ** 9 = '10,077,696'
txt = "6 ** 9 = {:,}"
print(txt.format(num1**num2))

#(num1, "**",num2,"=",num1**num2)6


