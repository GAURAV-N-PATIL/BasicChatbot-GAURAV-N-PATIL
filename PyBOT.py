# Basic ChatBot for DMX project 
import datetime
import random

# Time-based greeting
def time_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 17:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

# Help Menu
HELP_MESSAGE = """
I can understand the following commands:

- hello / hi / hey              → Greeting
- your name                     → Know my name
- how are you                   → Ask how I'm doing
- weather                       → Weather info
- joke                          → Hear a joke
- math (example: 2 + 2)         → Simple calculation
- help                          → Show help menu
- bye / exit                    → End the chat
"""

# Jokes list
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "My code works… I have no idea why.",
    "Debugging is like being a detective in your own code.",
    "I tried to learn Python… turns out it doesn’t bite.",
    "I would tell you a UDP joke… but you might not get it."
]
# Main Chatbot Function
def chatbot():
    print(time_greeting())
    print("Hello! I am a basic rule-based Python chatbot-PyBot 🤖")
    print("Type 'help' to see what I can do.\n")

    while True:
        user_input = input("You: ").lower().strip()
        words = user_input.split()

        # Exit command
        if user_input in ["bye", "exit"]:
            print("Bot: Goodbye! Have a great day 👋")
            break

        # Help command
        elif "help" in words:
            print(HELP_MESSAGE)

        # Greetings
        elif any(word in words for word in ["hi", "hello", "hey"]):
            print("Bot:", random.choice([
                "Hello there! 😊",
                "Hi! How can I help you?",
                "Hey! Nice to see you."
            ]))

        # Bot name
        elif "name" in words and "your" in words:
            print("Bot: I am a rule-based Python chatbot.")

        # How are you
        elif "how" in words and "you" in words:
            print("Bot: I'm doing great! Thanks for asking 😊")

        # Weather
        elif "weather" in words:
            print("Bot: I can't check live weather, but I hope it's nice outside!")

        # Joke
        elif "joke" in words:
            print("Bot:", random.choice(JOKES))

        # Math calculation
        elif any(op in user_input for op in ["+", "-", "*", "/"]):
            try:
                result = eval(user_input)
                print(f"Bot: The answer is {result}")
            except:
                print("Bot: Sorry, I couldn't calculate that.")

        # Default response
        else:
            print("Bot: Sorry, I didn’t understand that.")

# Program Start
if __name__ == "__main__":
    chatbot()
