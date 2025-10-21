def smart_grade_predictor(grades, attendance):
    if not grades:
        return "No grades available."
    avg_grade = sum(grades) / len(grades)
    weighted_score = (0.8 * avg_grade) + (0.2 * (attendance * 100))
    if weighted_score >= 90:
        performance = "Excellent"
    elif weighted_score >= 75:
        performance = "Good"
    elif weighted_score >= 60:
        performance = "Average"
    else:
        performance = "Needs Improvement"
    return {
        "Average Grade": round(avg_grade, 2),
        "Attendance %": round(attendance * 100, 1),
        "Weighted Score": round(weighted_score, 2),
        "Performance": performance
    }

grades = [85, 90, 70, 95, 88]
attendance = 0.92
result = smart_grade_predictor(grades, attendance)

print("SMART GRADE PREDICTOR RESULT")
for k, v in result.items():
    print(f"{k:20s}: {v}")
print("-" * 50)



