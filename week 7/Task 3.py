obt_marks = int(input("Enter your marks: "))
t_marks = int(input("Enter your total marks: "))
if (t_marks == 0) or (obt_marks == t_marks) :
    print("Invalid")

else:    
    percentage = (obt_marks/t_marks)*100
    print("Your percentage is:", percentage)


    if percentage >= 90:
        print("Grade: A")   
    elif percentage >= 85:
        print("Grade: A-")   
    elif percentage >= 80:
        print("Grade: B+")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: B-")
    elif percentage >= 65:
        print("Grade: C+")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 55:
        print("Grade: C-")
    elif percentage >= 50:
        print("Grade: D")

    else:
        print("Grade: F")

