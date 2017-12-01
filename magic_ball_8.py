import random

def intro():
    print("Welcome! You can ask any WHAT question. \n"
          "And 'Quit' to exit the game.")

def magic_ball():

    magic_reply = ["It is certain.",
        "Yes, definitely!",
        "Whoa! I... do not know.",
        "No, I am sorry!",
        "That is nonsense!",
        "Why?",
        "42",
        "I cannot find your answer in my system.",
        "Yes.",
        "Did you really want to ask that?",
        "Ab-so-lu-tly!",
        "No.",
        "Hahahaha, sure thing!",
        "You don’t want to know.",
        "Sure. Next!",
        "It is uncertain.",
        "No, not again. Come on!",
        "Cats. That is what you should be asking for.",
        "What a silly question!",
        "Out of order. Ask again later.",
        "I was not programmed to answer that."]

    response = input("What would you like to ask?: \n")

    while response != ("Quit").lower():
        print(random.choice(magic_reply))
        response = input("\nWhat is your next question?: \n")
    print("Thank you for playing!")


intro()
magic_ball()