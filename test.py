import speech_recognition as sr
import pyttsx3
import csv
import difflib
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
def match_score(description, user_input):
    return difflib.SequenceMatcher(None, description.lower(), user_input.lower()).ratio()
 
# Loop infinitely for user to speak
while(1):   
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ", MyText)
            # SpeakText(MyText)
             
            highest_match_score = 0
            highest_match_description = ""
            with open('blind75_mod.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    description = row['Description'].encode('ascii', 'ignore').decode().lower()
                    match_score_val = match_score(description, MyText)
                    if match_score_val > highest_match_score:
                        highest_match_score = match_score_val
                        highest_match_description = description
            print("The most similar question is: ", highest_match_description)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
