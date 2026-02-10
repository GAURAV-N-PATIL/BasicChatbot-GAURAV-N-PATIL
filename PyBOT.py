# Basic ChatBot for DMX project 
""" for this project i will be using a simple intent recognition system.
 it will same as my previous project (PyAssist https://github.com/GAURAV-N-PATIL/PyAssist-User-Response-Assistant.git)
"""
Userinput = input("Hello, I am PyBot, How can I help you? :) ")
# Normalization of user input
Userinput = Userinput.lower()
Userinput = Userinput.strip()
# Intent
Greeting_keywords = ["hello", "hi", "hey", "greetings","hey there","good morning","good afternoon","good evening","how are you","what's up","how's it going","hello there","hi PyBot"]
Exit_keywords = ["exit", "quit", "goodbye", "bye","see you later","take care","farewell","catch you later","talk to you later","have a nice day","have a good day"]
Identity_keywords = ["who are you", "what is your name", "what do you do", "what can you do","tell me about yourself","what's your name","what's your purpose","what's your function","what's your role"]
intent = "Unknown"
