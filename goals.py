def calculate_progress(hours_studied, study_goal):
    progress = (hours_studied / study_goal) * 100

    print("Goal Progress:", progress, "%")
    return progress


def check_goal(hours_studied, study_goal):

    print("Study goal:", study_goal)

    if hours_studied >= study_goal:
        print("Congratulations! You achieved your study goal!")
    else:
        remaining_hours = study_goal - hours_studied
        print("You need to study", remaining_hours,
              "more hours to reach your goal.")