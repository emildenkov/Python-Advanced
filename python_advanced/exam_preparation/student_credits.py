def students_credits(*courses_info):
    total_points = 0
    total_credits = {}
    final_print = []

    for data in courses_info:
        c_name, current_credits, max_points, dian_points = data.split("-")
        percentage = int(dian_points) / int(max_points)
        given_credits = int(current_credits) * int(percentage)
        total_points += given_credits
        total_credits[c_name] = given_credits

    if total_points >= 240:
        final_print.append(f"Diyan gets a diploma with {total_points:.1f} credits.")
    else:
        final_print.append(f"Diyan needs {240 - total_points:.1f} credits more for a diploma.")

    sorted_results = sorted(total_credits.items(), key=lambda x: (-x[1]))

    for course, initial_credits in sorted_results:
        final_print.append(f"{course} - {initial_credits:.1f}")

    return "\n".join(final_print)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
