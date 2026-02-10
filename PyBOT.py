# Basic ChatBot for DMX project 
""" for this project i will be using a simple intent recognition system.
 it will same as my previous project (PyAssist https://github.com/GAURAV-N-PATIL/PyAssist-User-Response-Assistant.git)
"""
# libraries Used
import datetime
import random

def get_time_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Pybot:Good Morning!"
    elif hour < 17:
        return "Pybot:Good Afternoon!"
    else:
        return "Pybot:Good Evening!"

def chatbot():
    print(get_time_greeting())
    print("Pybot:Hello! I am a PyBOT - basic Python chatbot.")

# Intent
Greeting_keywords = ["hello", "hi", "hey", "greetings","hey there","good morning","good afternoon","good evening","how are you","what's up","how's it going","hello there","hi PyBot"]
Exit_keywords = ["exit", "quit", "goodbye", "bye","see you later","take care","farewell","catch you later","talk to you later","have a nice day","have a good day"]
Identity_keywords = ["who are you", "what is your name", "what do you do", "what can you do","tell me about yourself","what's your name","what's your purpose","what's your function","what's your role"]
Weather_keywords = ["weather"]
intent = "Unknown"
chat_history = []

# Output response based on intent
def output_response(intent):

    if intent == "Exit":
        response = "Pybot:Goodbye! Have a great day 😊"
        print("PyBot:", response)
        chat_history.append(response)
        exit()

    elif intent == "Greeting":
         response = random.choice([
                "Pybot:Hello there!",
                "Pybot:Hi! How can I help you?",
                "Pybot:Hey! Nice to see you."
            ])
         
    elif intent == "Identity":
        response = "Pybot:I am PyBot, your personal assistant designed to help you with various tasks."

    elif intent == "Weather":
        response = "Pybot:I can't check live weather, but I hope it's nice outside!"

    else:
        response = "Pybot:I'm sorry, I didn't understand that command."

    print(response)
    chat_history.append(response)
# respond to user input
chatbot()
while intent not in Exit_keywords:

    # Normalization of user input
    Userinput = input("You:")
    Userinput = Userinput.lower()
    Userinput = Userinput.strip()
    chat_history.append(f"You: {Userinput}")

    # Intent recognition
    if Userinput in Greeting_keywords:
        intent = "Greeting"
    elif Userinput in Exit_keywords:
        intent = "Exit"
    elif Userinput in Identity_keywords:
        intent = "Identity"
    elif Userinput in Weather_keywords:
        intent = "Weather"
    elif Userinput == "help":
        print("Pybot:enter \"weather\" to check get info on weather")
    elif Userinput == "tell me joke":
            print(random.choice([
                "Pybot:Why do programmers prefer dark mode? Because light attracts bugs. 🐛",
                "Pybot:Why did the Python programmer wear glasses? Because they couldn’t C.",
                "Pybot:I tried to learn Python… Turns out it doesn’t bite. 🐍",
                "Pybot:Why was the computer cold? It forgot to close its Windows.",
                "Pybot:Why do Java developers wear glasses? Because they don’t C#."
            ]))

    #respond to user input based on intent
    output_response(intent)

    # Save conversation history
    with open("chat_history.txt", "w") as file:
        for line in chat_history:
            file.write(line + "\n")

# main function            
if __name__ == "__main__":
    chatbot()