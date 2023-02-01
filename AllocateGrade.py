#Exercise 1 – Write a Python program called AllocateGrade.py that accepts a number from the user representing a student grade for an exam, and prints the appropriate grade using the scale:

#93 <= A <= 100

#85 <= B < 93

#75 <= C+ < 85

#65 <= C < 75

#55 <= C- < 65

#40 <= D < 55

#0 <= F < 40

 #For example, if the user entered 57, the program would print:

   #'Your raw score is 57.0 so your grade is C- '


grade = float(input("Enter students raw grade: "))

if(grade >= 93 and grade <= 100):
    #print ("So your grade is: A")
    letter = 'A' 
elif(grade >= 85 and grade < 93):
    #print("B")
    letter = 'B' 
elif(grade >= 75 and grade < 85):
    #print("C+")
    letter = 'C+' 
elif(grade >= 65 and grade < 75):
   #print("C")
   letter = 'C' 
elif(grade >= 55 and grade < 65):
    #print("C-")
    letter = 'C-' 
elif(grade >= 40 and grade < 55):
    #print("D")
    letter = 'D' 
elif(grade >= 0 and grade < 40):
    #print("F")
    letter = 'F'
else:
    print("Invalid Grade")

#print("AllocateGrade"(grade))
print("Your raw score is:", grade,"So your grade is:", letter)