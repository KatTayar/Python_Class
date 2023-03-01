#Kathryn Tayar
# Date: Feb 15, 2023
#Write a program named TestPrimes that prints the first 200 primes, 20 primes per row. A prime number is an integer that is divisible by 1 and itself. To complete this exercise:

#1.     First write a loop that tests an integer n if it is prime as follows. Divide the integer by every integer starting at 2 up to one less than n.
#       a.      If the remainder of any division is zero, then the number is not prime so break out of the loop.

#       b.     If the remainder of all divisions is non-zero, then the number is prime so print it.

#2.     Second, add an outer loop that iterates from 2 to some large value.

#       a.      Pass the loop variable from the outer loop as the value the inner loop tests for primeness.

#       .     Add other code as is necessary.

#STEP2: Modify your TestPrimes program so that it prints 200 primes starting from a minimum value up to a maximum value, 20 primes per row.
#input integer to test for primeness

#num = int(input("Enter a positive integer: "))

import math
MAXrange = 123456789
MINrange = 1123456789
primeCount = 0
totalPrimes = 0
for n in range(MINrange, MAXrange):
    isPrime = True
    for divisor in range(2, round(math.sqrt(n))):
        if(n % divisor == 0):
            isPrime = False
        break
    if(isPrime and n > 1):
        print(n, end = " ") 
    primeCount += 1
    totalPrimes += 1
    if(primeCount == 20): 
        print()
    primeCount = 0
    if(totalPrimes == 200):
        break