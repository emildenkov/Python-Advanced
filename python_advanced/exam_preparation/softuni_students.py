def softuni_students(*id_username, **course_info):
    invalid_students = set()
    course_students = {}

    for data in id_username:
        student_id, name = data

        if student_id not in course_info.keys():
            invalid_students.add(name)
        else:
            course_name = course_info[student_id]
            course_students[name] = course_name

    sorted_students = sorted(course_students.items())
    result = []

    for student, course in sorted_students:
        result.append(f"*** A student with the username {student} has successfully finished the course {course}!")

    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    return "\n".join(result)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
