# Read marks for three subjects
marks1 = int(input("Enter marks in first subject : "))
marks2 = int(input("Enter marks in second subject : "))
marks3 = int(input("Enter marks in third subject : "))

# Check if student passes in all subjects
if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
    print("Pass")
else:
    print("Fail")
