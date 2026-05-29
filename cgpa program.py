print("This program computes a student's cgpa for six courses")
score_map={'A':5.0, 'B':4.0, 'C':3.0, 'D':2.0, 'F':0.0}
total_points=0.0
total_units=0
for i in range(6):
    grade=input(f"Enter grade for course {i+1}: ").upper()
    unit=int(input(f"Enter credit unit for course {i+1} "))

    if grade in score_map:
        point=score_map[grade]
        total_points += point*unit
        total_units += unit
    else:
        print("Invalid grade")

if total_units==0:
        print("No valid courses entered")
else:
    cgpa=total_points/total_units
    print(f"Your GPA is : {cgpa}")