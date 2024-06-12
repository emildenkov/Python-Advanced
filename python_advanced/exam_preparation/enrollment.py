def gather_credits(n_credits, *courses_info):
    score = 0
    courses_name = {}

    for name, points in courses_info:
        if score >= n_credits:
            break

        if name not in courses_name:
            courses_name[name] = points
            score += points

    if score >= n_credits:
        return f"Enrollment finished! Maximum credits: {score}.\nCourses: {', '.join(sorted(courses_name))}"
    return f"You need to enroll in more courses! You have to gather {n_credits - score} credits more."


print(gather_credits(
	80,
	("Advanced", 30),
	("Basics", 27),
	("Fundamentals", 27),
))
