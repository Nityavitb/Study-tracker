from study_tracker import get_student_details
from goals import calculate_progress, check_goal
from checklist import create_checklist
from reports import generate_report


name, hours_studied, study_goal, subject, topic = get_student_details()

to_do, checklist = create_checklist()

study_sessions = int(input("How many study sessions have you completed? "))

print("Total study sessions:", study_sessions)

check_goal(hours_studied, study_goal)

progress = calculate_progress(hours_studied, study_goal)

generate_report(
    name,
    subject,
    topic,
    hours_studied,
    study_goal,
    study_sessions,
    progress,
    to_do,
    checklist
)