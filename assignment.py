students = {
    1: {"name": "Deepak", "age": 19, "marks": 92},
    2: {"name": "Charan", "age": 19, "marks": 91},
    3: {"name": "Thanush", "age": 19, "marks": 89},
    4: {"name": "Nagesh", "age": 19, "marks": 90},
    5: {"name": "Student", "age": 19, "marks": 82}
}

for student_id, detailes in students.items():
    print(f"Student-ID: {student_id} & Name: {detailes["name"]} ; age: {detailes["age"]} - Marks is {detailes["marks"]}")