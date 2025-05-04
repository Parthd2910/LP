# Expert System for Employee Performance Evaluation

def get_performance_score(punctuality, quality_of_work, teamwork, initiative):
    score = 0

    # Rule 1: Punctuality
    if punctuality == "Excellent":
        score += 25
    elif punctuality == "Good":
        score += 20
    elif punctuality == "Average":
        score += 15
    else:
        score += 10

    # Rule 2: Quality of Work
    if quality_of_work == "Excellent":
        score += 30
    elif quality_of_work == "Good":
        score += 25
    elif quality_of_work == "Average":
        score += 20
    else:
        score += 15

    # Rule 3: Teamwork
    if teamwork == "Excellent":
        score += 20
    elif teamwork == "Good":
        score += 15
    elif teamwork == "Average":
        score += 10
    else:
        score += 5

    # Rule 4: Initiative
    if initiative == "High":
        score += 25
    elif initiative == "Moderate":
        score += 15
    else:
        score += 10

    return score

def evaluate_performance(score):
    if score >= 85:
        return "Outstanding"
    elif score >= 70:
        return "Very Good"
    elif score >= 55:
        return "Good"
    elif score >= 40:
        return "Needs Improvement"
    else:
        return "Unsatisfactory"

# --- User Interface ---
print("Employee Performance Evaluation System")

punctuality = input("Enter punctuality (Excellent/Good/Average/Poor): ")
quality_of_work = input("Enter quality of work (Excellent/Good/Average/Poor): ")
teamwork = input("Enter teamwork (Excellent/Good/Average/Poor): ")
initiative = input("Enter initiative (High/Moderate/Low): ")

score = get_performance_score(punctuality, quality_of_work, teamwork, initiative)
performance = evaluate_performance(score)

print(f"\nTotal Score: {score}")
print(f"Performance Rating: {performance}")
