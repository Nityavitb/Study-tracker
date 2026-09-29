def get_student_details():

   print("Welcome to the Study Hours Tracker!")
   study_sessions=[]
   name = input("Enter your name and start tracking your study hours: ")
   print("WELCOME",name)
   hours_studied = float(input("Add study hours: "))
   study_goal = float(input("Set your study goal in hours: "))
   print("You have studied for", hours_studied, "hours.")
   print("Your study goal is", study_goal, "hours.")
   subject = input("Enter the subject you studied: ")
   topic = input("Enter the topic you studied: ")
   return name, hours_studied, study_goal, subject, topic