import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

print("Voice Assistant Started")
print("Type: hello, time, date, exit")

while True:
    command = input("You: ").lower()

    if command == "hello":
        response = "Hello! How can I help you?"

    elif command == "time":
        response = "Current time is " + datetime.now().strftime("%H:%M:%S")

    elif command == "date":
        response = "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif command == "exit":
        response = "Goodbye!"
        print("Assistant:", response)
        engine.say(response)
        engine.runAndWait()
        break

    else:
        response = "Sorry, I don't understand."

    print("Assistant:", response)

    engine.say(response)
    engine.runAndWait()