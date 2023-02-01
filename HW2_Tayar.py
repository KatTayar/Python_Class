#PART A: Write a Python program that reads three integers from the keyboard and 
# computes and prints:

#The sum of the three integers.
#The average of the three integers.
#The square of the smallest integer.
#The factorial of the middle integer.
#The square root of the largest integer.
 
#After the numbers have been read and the sum, average, square, factorial, and 
# square root have been computed, the program should print output of the following form:

 #Thanks for your input.
#The smallest integer entered was xxx.
#The square of xxx is yyy.
#The middle integer is zzzz.
#The factorial of zzzz is aaa.
#The largest integer entered was www.
#The square root of www is yyy.yy
import math


num1 = int(input("Enter First Integer: "))
num2 = int(input("Enter Second Integer: "))
num3 = int(input("Enter Third Integer: "))
sumofint = num1 + num2 + num3
print("This is the sum of three Integers", sumofint)

avgofint = sumofint / 3
print("This is the average of three Integers", avgofint)

if num1 <= num2 and num1 <= num3:
        smallint = num1
elif num2 <= num1 and num2 <= num3:
        smallint = num2
else:
     num3 <= num1 and num3 <= num2
     smallint = num3
#square = smallint 

print("The Square of the smallest integer is",(math.pow(smallint, 2)))

if num1 >= num2 and num1 <= num3:
        midint = num1
elif num2 >= num1 and num2 <= num3:
        midint = num2
else:
     num3 >= num1 and num3 <= num2
     midint = num3        
#print(midint)
print("The factoral of the middle integer is", math.factorial(midint))

if num1 > num2 and num1 > num3:
        lgint = num1
elif num2 > num1 and num2 > num3:
        lgint = num2
elif num3 > num1 and num3 > num2:
     lgint = num3        
else:
    num1 == num2 and num2 == num3
    lgint = num1
     #print(lgint)
print("The Square root of the largest integer is", math.sqrt(lgint))