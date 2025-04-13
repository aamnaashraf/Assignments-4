# Weekend Fun Story with Two Characters

def get_words():
    print("Welcome to Mad Libs! Let's create a fun weekend story.")
    name1 = input("Enter the first character's name: ")
    name2 = input("Enter the second character's name: ")
    place = input("Enter a place for the weekend trip: ")
    activity1 = input("Enter a fun activity (e.g., hiking, dancing): ")
    food = input("Enter a favorite food: ")
    vehicle = input("Enter a vehicle (e.g., car, bike): ")
    emotion = input("Enter an emotion (e.g., excited, happy): ")
    surprise = input("Enter a surprise element (e.g., rainbow, treasure): ")
    return name1, name2, place, activity1, food, vehicle, emotion, surprise

def generate_story(name1, name2, place, activity1, food, vehicle, emotion, surprise):
    story = f"""
    Last weekend, {name1} and {name2} decided to go on a fun trip to {place}.
    They packed their favorite {food} and hopped into their {vehicle} for the journey.
    When they reached {place}, they started {activity1} and had the time of their lives!
    Suddenly, they saw a {surprise} and couldn't believe their eyes.
    They felt {emotion} and spent the rest of the day exploring and enjoying every moment.
    It was a weekend they would never forget!
    """
    return story

def mad_libs_game():

    name1, name2, place, activity1, food, vehicle, emotion, surprise = get_words()


    story = generate_story(name1, name2, place, activity1, food, vehicle, emotion, surprise)
    print("\nHere's your Mad Libs story:\n")
    print(story)


mad_libs_game()