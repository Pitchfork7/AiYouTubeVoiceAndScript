from duckai import DuckAI
import wikipedia
import pyttsx3
engine = pyttsx3.init()


wikitopic = input("Wikipedia page> ")
wikitopic = wikipedia.page(str(wikitopic))
say = input("Do you want to have the script as mp3(y/n)> ")


results = DuckAI().chat(f"Create a video script for a youtube video, only respond with the script and no other dialog, the script should only use the information from the string {wikitopic}")
with open("script.txt", "w") as f:
  f.write(results)
print(results)

if say = "y":
  engine.save_to_file(results, 'speech.mp3')

  engine.runAndWait()


