print("Please put in info of your student")
print("-------------------------------------------")
#defining information
print("Format (Firstname lastname,Course)")
stud_name,stud_course = input("Enter Student name and Course: ").split()
print("-------------------------------------------")
#defining Grades(Used this Class Grading System)
prelim_attendance = int(input("Enter Students Prelim Attendance Grade: "))
print("-------------------------------------------")
#Defining how many quizzes and the exam score for the period
qt=int(input("Enter the number of quizzes taken this sem: "))#get the number of quizzes taken and average
a=[]
for i in range(0,qt):
    quiz=int(input("Enter Quiz: "))
    a.append(quiz)
prelim_quiz_avg=sum(a)/qt
print("Average of Quizzes in the sem: ",round(prelim_quiz_avg,2))
print("-------------------------------------------")
#computing according to this subjects grading system
prelim_Class_Standing = prelim_quiz_avg*0.9+prelim_attendance*0.1
pre_exam_grade=int(input("Enter Prelim Exam Score: "))
prelim_Grade = prelim_Class_Standing*0.70+pre_exam_grade*0.30
prelim_Grade_perc = "{:.2f}".format(prelim_Grade)#conver the grade to 2 decimal points
if float(prelim_Grade_perc) < 70.01:
    print("\U0001F600")
elif float(prelim_Grade_perc) >= 70.00:
    print("\U0001F606")
elif float(prelim_Grade_perc) > 69.99:
    print("\U0001F62D")
print(f"{prelim_Grade_perc } is your prelim Grade")
print("-------------------------------------------")

#Computing Midterm quiz using for loop i sued on prelim
print("Input Midterm scores")
midterm_attendance = int(input("Enter Students Midterm Attendance Grade: "))
print("-------------------------------------------")
qt=int(input("Enter the number of quizzes taken this Midterm: "))
a=[]
for i in range(0,qt):
    quiz=int(input("Enter Quiz: "))
    a.append(quiz)
midterm_quiz_avg=sum(a)/qt
print("Average of Quizzes in the midterm",round(midterm_quiz_avg,2))
#Computing Midterm Grade
midterm_Class_Standing = midterm_quiz_avg*0.9+midterm_attendance*0.1
midterm_exam_grade=int(input("Enter Midterm Exam Score"))
midterm_Grade = midterm_Class_Standing*0.70+midterm_exam_grade*0.30
midterm_Grade_perc = "{:.2f}".format(midterm_Grade)#conver the grade to 2 decimal points
if float(midterm_Grade_perc) < 70.01: #helps the program identify which emoji to use
    print("\U0001F600")
elif float(midterm_Grade_perc) >= 70.00:
    print("\U0001F606")
elif float(midterm_Grade_perc) > 69.99:
    print("\U0001F62D")
print(f"{midterm_Grade_perc} is your Midterm Grade")
print("-------------------------------------------")
print("Input Final scores")
#Computing Finals Grade
finals_attendance = int(input("Enter Students Finals Attendance Grade"))
print("-------------------------------------------")
qt=int(input("Enter the number of quizzes taken this Finals: "))
a=[]
for i in range(0,qt):
    quiz=int(input("Enter Quiz: "))
    a.append(quiz)
finals_quiz_avg=sum(a)/qt
print("Average of Quizzes in the Finals",round(finals_quiz_avg,2))

print("-------------------------------------------")
#Computing Finals Grade
finals_Class_Standing = finals_quiz_avg*0.9+finals_attendance*0.1
finals_exam_grade=int(input("Enter Finals Exam Score"))
finals_Grade = finals_Class_Standing*0.70+finals_exam_grade*0.30
finals_Grade_perc = "{:.2f}".format(finals_Grade)#convert the grade to 2 decimal points
if float(finals_Grade_perc) > 70.01:   #helps the program identify which emoji to use
    print("\U0001F600")
elif float(finals_Grade_perc) <= 70.00:
    print("\U0001F606")
elif float(finals_Grade_perc) < 69.99:
    print("\U0001F62D")
print(f"{finals_Grade_perc} is your finals Grade")
print("-------------------------------------------")
#Computing Semestral Grade
semestral_grade = float(prelim_Grade_perc)*0.30+float(midterm_Grade_perc)*0.30+float(finals_Grade_perc)*0.40
semestral_grade_perc="{:.2f}".format(semestral_grade)
if float(semestral_grade_perc) < 70.01: #helps the program identify which emoji to use
    print("\U0001F600")
elif float(semestral_grade_perc) >= 70.00:
    print("\U0001F606")
elif float (semestral_grade_perc) > 69.99:
    print("\U0001F62D")
print(f"your Student { stud_name } and his course { stud_course } has a Grade of { semestral_grade_perc } ")


_author = "Nicanor JImenez"
_copyright = "Copyright (C) 2021"
