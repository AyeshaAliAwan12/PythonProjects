#Example 01
ef ayesha():
    print("i am ayesha ali ")
    print("i'm always depressed")
    print("because i am over sensitive")
    print("i never understand why people so easily hurt each other by their words ,why they don't thinks about others?")

ayesha()
ayesha()
ayesha()
ayesha()
ayesha()
#Example 02
def argument(price):
    if  price==6:
        print("1 candy")
        print("1 ice cream")
        print("1 chocolate")
    if  price==12:
        print("2 candy")
        print("2 ice cream")
        print("2 chocolate")

argument(12)
#example 03
def exercise_mood(exercise_minutes, target_minutes):
    print(f"Exercise Minutes: {exercise_minutes}")
    print(f"Target Minutes: {target_minutes}")

    if exercise_minutes < target_minutes:
        print("I feel disappointed. I didn’t reach my exercise goal today.")
    elif exercise_minutes == target_minutes:
        print("I feel satisfied. I met my goal exactly.")
    else:
        print("I feel proud! I exceeded my exercise goal today.")

exercise_mood(45, 60)
