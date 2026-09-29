def create_checklist():

    to_do=input("Enter your to-do list for the next study session: ")
    checklist={
    "math": input("Enter your math to-do list: "),
    "programming": input("Enter your programming to-do list: "),
    "english": input("Enter your english to-do list: "),
    "electronics": input("Enter your electronics to-do list: ")
     }

    for x in checklist:
        print("Enter status of completion for", x, "to-do list is:", checklist[x])
    return to_do, checklist