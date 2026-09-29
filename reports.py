def generate_report(name, subject, topic, hours_studied,
                    study_goal, study_sessions, progress,
                    to_do, checklist):

    print("\n STUDY SESSION SUMMARY ")

    print("Student Name:", name)
    print("Subject Studied:", subject)
    print("Topic Studied:", topic)
    print("Hours Studied:", hours_studied)
    print("Study Goal:", study_goal)
    print("Total Sessions Completed:", study_sessions)

    print("Goal Progress:", progress, "%")

    if progress >= 100:
        print("Status: Goal Achieved!")
    else:
        print("Status: Goal In Progress")

    print("\n TO-DO LIST ")

    print("General To-Do:", to_do)

    for x in checklist:
        print(x, ":", checklist[x])

    print("\nThank you for using the Study Hours Tracker!")
    print("Keep studying and stay consistent!")