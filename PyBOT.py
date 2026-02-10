# Basic ChatBot for DMX project 
""" for this project i will be using a simple intent recognition system.
 it will same as my previous project (PyAssist https://github.com/GAURAV-N-PATIL/PyAssist-User-Response-Assistant.git)
"""
# Intent
Greeting_keywords = ["hello", "hi", "hey", "greetings","hey there","good morning","good afternoon","good evening","how are you","what's up","how's it going","hello there","hi PyBot"]
Exit_keywords = ["exit", "quit", "goodbye", "bye","see you later","take care","farewell","catch you later","talk to you later","have a nice day","have a good day"]
Identity_keywords = ["who are you", "what is your name", "what do you do", "what can you do","tell me about yourself","what's your name","what's your purpose","what's your function","what's your role"]
intent = "Unknown"
# Output response based on intent
def output_response(intent):
    if intent == "Greeting":
        print("Hello there! I'm PyBot. How can I help you today?")
    elif intent == "Exit":
        print("Goodbye! Have a great day!")
        exit()
    elif intent == "Identity":
        print("I am PyBot, your personal assistant designed to help you with various tasks.")
    else:
        print("I'm sorry, I didn't understand that command.")
# respond to user input
while intent not in Exit_keywords:
    # Normalization of user input
    Userinput = input("Hello, I am PyBot, How can I help you? :) ")
    Userinput = Userinput.lower()
    Userinput = Userinput.strip()
    # Intent recognition
    if Userinput in Greeting_keywords:
        intent = "Greeting"
    elif Userinput in Exit_keywords:
        intent = "Exit"
    elif Userinput in Identity_keywords:
        intent = "Identity"
    #respond to user input based on intent
    output_response(intent)
