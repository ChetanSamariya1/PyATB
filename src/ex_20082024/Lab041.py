# Grade Calculator
# Write a program that calculates and displays the letter grade
# for a given numerical score ( A, B, C, D or F)
# based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# LogiC Building Formula

# Step 1: User Input -> Score -> Int
# OutPut -> Grade -> String

#Step 2: Rough Logic
# enter the score and get the grade

# Step 3: Write the logic

score = int(input("Enter your score here\n"))

if score >= 90 and score <= 100:
    grade = "A"
    print(f"For score {score}, Your Grade is", grade)
elif score >= 80 and score <= 89:
    grade = "B"
    print(f"For score {score}, Your Grade is", grade)
elif score >= 70 and score <= 79:
    grade = "C"
    print(f"For score {score}, Your Grade is", grade)
elif score >= 60 and score <= 69:
    grade = "D"
    print(f"For score {score}, Your Grade is", grade)
else:
    grade = "F"
    print(f"For score {score}, Your Grade is", grade)
