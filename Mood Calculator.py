print("This program gives advice based on mood and energy levels")
mood= input("What mood are you in? Happy, Sad, Fear, Anger, Disgust, Surprise ")
energy = int(input("What number describes your energy Level, pick between 1-10 "))

def give_advice_for_mood(mood):
    """
    Accepts a string representing a mood, normalizes it, 
    and returns advice based on Paul Ekman's 6 universal emotions.
    """
    print("For Today's mood the advice is: ")
    normalized_mood = mood.lower().strip()
    if normalized_mood == "happy":
        return "Note what you Liked about this day, so you can look back on it whenever you're sad"
    elif normalized_mood == "sad":
        return "Take a walk outside and listen to some music."
    elif normalized_mood == "fear":
        return "Watch a cartoon"
    elif normalized_mood == "anger":
        return "Have you tried chilling out?"
    elif normalized_mood == "disgust":
        return "Run!"
    elif normalized_mood == "surprise":
        return "Was it good or bad? Enjoy"
    else:
        return "Please pick an emotion in the list"
    
def give_advice_for_energy(energy):
    """
    Docstring for give_advice_for_energy
    :param energy: Gives advice based on energy levels
    """
    print("For Today's energy level the advice is: ")
    if (energy < 0):
        return "Are you on lifesupport?"
    elif (energy < 5):
        return " Go rest"
    elif (energy <= 8):
        return "You're okay"
    elif (energy <=10):
        return "Must be nice"
    else:
        return "Girl choose a valid number"
    
print(give_advice_for_mood(mood))
print(give_advice_for_energy(energy))