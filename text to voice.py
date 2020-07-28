import pyttsx3
engine =pyttsx3.init()
print("Enter your words")
while(True):
    text = (input())
    if text=="Exit" or text =='exit':
        engine.say("Thanks for seeing my code. Hope you had liked it")
        engine.runAndWait()
        break
    else:
        engine.say(text)
        engine.runAndWait()
