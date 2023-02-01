#Exercise 2: Write a program called RomanNumerals.py “that prompts the user to enter a number within the range of 1 through 10. The program should display the Roman numeral version of the number entered. If the number entered is outside the range of 1 through 10, the program should display an error message. The following table shows the Roman numerals for the numbers 1 through 10.” 

              #Number      Roman Numeral

             # 1                           I

              #2                           II

              #3                           III

              #4                           IV

              #5                           V

              #6                           VI

              #7                           VII

              #8                           VIII

              #9                           IX

              #10                         X

#For example, if the user entered 7, the program would print:
 #  'Decimal 7 corresponds with Roman numeral VII'
#Problem adapted from Gaddis textbook Programming Exercise 4.1

num = int(input("Enter a number between 1 - 10: "))

if(num == 1):
    #print ("I")
    roman = 'I'
elif(num == 2):
    #print("II")
    roman = 'II'
elif(num == 3):
    #print("III")
    roman = 'III'
elif(num == 4):
   #print("IV")
   roman = 'IV'
elif(num == 5):
    #print("V")
    roman = 'V'
elif(num == 6):
    #print("VI")
    roman = 'VI'
elif(num == 7):
    #print("VII")
    roman = 'VII'
elif(num == 8):
    #print("VIII")
    roman = 'VIII'
elif(num == 9):
    #print("IX")
    roman = 'IX'
elif(num == 10):
    #print("X")
    roman = 'X'
else:
    print("Invalid Number either lower or higher than 10")

print("You entered the number:", num, "And its roman numeral form is:", roman)
    
    