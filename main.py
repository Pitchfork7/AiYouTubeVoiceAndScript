from duckai import DuckAI
import wikipedia
import pyttsx3
engine = pyttsx3.init()


wikitopic = input("Wikipedia page> ")
wikitopic = wikipedia.page(str(wikitopic))
wikititle = wikitopic.title
wikilength = input("Enter the number of minutes you want your scipt to be> ")
say = input("Do you want to have the script as mp3(y/n)> ")

#tts settings
if input("Change speaking speed(y/n)> ") == "y":
  try:
    engine.setProperty("rate", int(input("Speed(default is 125)> ")))
    ttsspeed = engine.getProperty("rate")
  except:
    print("Rate setting failed, defaulting to 125")
    engine.setProperty("rate", 125)
    ttsspeed = engine.getProperty("rate")
  else:
    ttsspeed = engine.getProperty("rate")
    

voicetype = input("Set voice(m/f)")
if voicetype == "m":
  engine.setProperty('voice', voices[0].id)
elif voicetype == "f":
  engine.setProperty('voice', voices[1].id)
else:
  print("Voice setting unrecognized, setting to male")
  engine.setProperty('voice', voices[0].id)

voicevolume = float(input("Set voice(int)> "))
try:
  engine.setProperty("volume",voicevolume)
except:
  print("Volume not being set, defaulting to 1.0")
  engine.setProperty("volume", 1.0)

results = DuckAI().chat(f"Act as a professional scriptwriter for TTS (Text-to-Speech). Your task is to write a cohesive video script about {wikititle} using only the information from the string {wikitopic}, the script should last around {wikilength} minutes long . CONSTRAINTS: 1. Write exclusively in continuous paragraph form.  2. Do NOT use scene headings (e.g., [Scene 1]), visual cues (e.g., [B-roll of a forest]), or timestamps. 3. Do NOT include any introductory or concluding conversational filler (e.g., Here is the script you requested). 4. Ensure the flow is natural for spoken audio. Output ONLY the final script text. Settings for the tts are Speaking Rate: {str(ttsspeed)}")

with open("script.txt", "w") as f:
  f.write(results)
print(results)

if say == "y":
  engine.save_to_file(results, 'speech.mp3')

  engine.runAndWait()


