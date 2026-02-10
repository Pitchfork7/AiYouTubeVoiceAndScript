from duckai import DuckAI
import wikipedia
import pyttsx3
engine = pyttsx3.init()


wikitopic = input("Wikipedia page> ")
wikitopic = wikipedia.page(str(wikitopic))
say = input("Do you want to have the script as mp3(y/n)> ")


results = DuckAI().chat(f"Act as a professional scriptwriter for TTS (Text-to-Speech). Your task is to write a cohesive video script about {wikitopic}. CONSTRAINTS: 1. Write exclusively in continuous paragraph form.  2. Do NOT use scene headings (e.g., [Scene 1]), visual cues (e.g., [B-roll of a forest]), or timestamps. 3. Do NOT include any introductory or concluding conversational filler (e.g., Here is the script you requested). 4. Ensure the flow is natural for spoken audio."

Output ONLY the final script text.
Create a video script for a youtube video, only respond with the script and no other dialog, the script should only use the information from the string {wikitopic}")
with open("script.txt", "w") as f:
  f.write(results)
print(results)

if say == "y":
  engine.save_to_file(results, 'speech.mp3')

  engine.runAndWait()


