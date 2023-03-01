#Function 1: A function named makeList(n) that creates and returns a list of grades for an exam. The function takes a single integer parameter n, 
#representing the number of grades to be generated. Each grade is obtained by randomly generating a floating-point value between 30 and 100.

def makeList():
    pass

#Function 2: function findGreatest(scoreList) that accepts a list of exam scores as parameter and returns a tuple consisting of the largest score in
# scoreList and its position in the list.

def findGreatest(scoreList):
    pass

#Function 3: A function findSmallest(scoreList) that accepts a list of exam scores as parameter and returns a tuple consisting of the smallest score
#  in scoreList and its position in the list

def findSmallest(scoreList):
    pass

#Function 4: A function aboveScore(scoreList, minScore) that takes a list of scores and a minimum score as parameters, 
# and returns a new list of all scores greater than minScore.

def aboveScore(scoreList, minScore):
    pass

#Function 5: A function belowScore(scoreList, maxScore) that takes a list of scores and a maximum score as parameters, 
# and returns a new list of all scores less than maxScore.

def belowScore(scoreList, minScore):
    pass

#Function 6: A function insertGrades(examScores, n) that takes two parameters, a list of exam scores and the number of scores to be inserted. 
# For each score to be inserted, the function will ask the user for the score, and the position where the score is to be inserted. The function does not return a value.

def insertGrades(examScores, n):
    pass

#Function 7: A function named gradeExam(examScores) that receives a list of exam scores as a parameter and creates and returns a new list consisting of pairs of scores 
# and corresponding letter grade. For example, if the input list is: [70, 85, 90, 94, 87, 66], 
# the function would return the list: [(70, C), (85, B), (90, A), (94, A), (87, B), (66, D)]. Note that each entry in the table is a tuple.
#  The function uses the following grading scale:      
#Score                              Letter Grade
#---------------------------------------------------------------------
#90 – 100                                   A      
#80 – 89                                     B
#70 – 79                                     C
#60 – 69                                     D
#Below 60                                  F

def gradeExams(examScores):
    pass

#Function 8: A main function main that tests the functions as follows: (1) calls makeList, then use the list returned to call the other functions.
#  The main method should print an appropriate message after each function call to show the state of the list after each call.

def main():
    print(__doc__)
    print("makeList(n):", makeList.__doc__)


    pass



 