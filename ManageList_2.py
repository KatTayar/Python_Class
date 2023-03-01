import random

def makeList(n):
    return [random.uniform(30, 100) for _ in range(n)]

def findGreatest(scoreList):
    greatest_score = max(scoreList)
    position = scoreList.index(greatest_score)
    return (greatest_score, position)

def findSmallest(scoreList):
    smallest_score = min(scoreList)
    position = scoreList.index(smallest_score)
    return (smallest_score, position)

def aboveScore(scoreList, minScore):
    return [score for score in scoreList if score > minScore]

def belowScore(scoreList, maxScore):
    return [score for score in scoreList if score < maxScore]

def insertGrades(examScores, n):
    for i in range(n):
        score = float(input("Enter score to insert: "))
        position = int(input("Enter position to insert score: "))
        examScores.insert(position, score)

def gradeExam(examScores):
    grade_scale = {90: "A", 80: "B", 70: "C", 60: "D"}
    graded_scores = []
    for score in examScores:
        for grade in grade_scale.keys():
            if score >= grade:
                graded_scores.append((score, grade_scale[grade]))
                break
        else:
            graded_scores.append((score, "F"))
    return graded_scores

def main():
    scores = makeList(10)
    print(f"Generated list of scores: {scores}")

    greatest_score, position = findGreatest(scores)
    print(f"The greatest score is {greatest_score} at position {position}")

    smallest_score, position = findSmallest(scores)
    print(f"The smallest score is {smallest_score} at position {position}")

    min_score = float(input("Enter a minimum score to find scores greater than: "))
    above_scores = aboveScore(scores, min_score)
    print(f"Scores greater than {min_score}: {above_scores}")

    max_score = float(input("Enter a maximum score to find scores less than: "))
    below_scores = belowScore(scores, max_score)
    print(f"Scores less than {max_score}: {below_scores}")

    num_inserts = int(input("Enter the number of scores to insert: "))
    insertGrades(scores, num_inserts)
    print(f"List after inserting scores: {scores}")

    graded_scores = gradeExam(scores)
    print(f"Graded scores: {graded_scores}")

if __name__ == "__main__":
    main()
