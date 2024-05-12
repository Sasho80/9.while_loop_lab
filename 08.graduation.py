name = input()

GRADE = 1
sum_marks = 0.0
excluded = 0
average_grade = 0.0

while GRADE < 13:
    marks = float(input())
    if marks >= 4:
        sum_marks += marks
        GRADE += 1
    else:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {GRADE} grade")
            break
    continue
else:
    average_grade = sum_marks / (GRADE - 1)
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
