from duckai import DuckAI
import wikipedia
import wave
from piper.voice import PiperVoice

try:
    model = "en_US-amy-medium.onnx"
    config = "en_US-amy-medium.onnx.json"
    voice = PiperVoice.load(model, config_path=config)
except:
    print("Error, voice missing, go to https://huggingface.co/rhasspy/piper-voices/tree/main to get voices.")

wikitopic = input("Wikipedia page> ")
wikitopic = wikipedia.page(str(wikitopic))
wikititle = wikitopic.title
wikilength = input("Enter the number of minutes you want your scipt to be> ")
say = input("Do you want to have the script as wave(y/n)> ")

#tts settings
if input("Change speaking speed(y/n)> ") == "y":
    ttsspeed = float(input("Speed(default is 1.0)> "))
else:
    ttsspeed = 1.0


results = DuckAI().chat(f"Act as a professional scriptwriter for TTS (Text-to-Speech). Your task is to write a cohesive video script about {wikititle} using only the information from the string {wikitopic}, the script should last around {wikilength} minutes long . CONSTRAINTS: 1. Write exclusively in continuous paragraph form.  2. Do NOT use scene headings (e.g., [Scene 1]), visual cues (e.g., [B-roll of a forest]), or timestamps. 3. Do NOT include any introductory or concluding conversational filler (e.g., Here is the script you requested). 4. Ensure the flow is natural for spoken audio. Output ONLY the final script text. Settings for the tts are Speaking Speed the lower the faster: {str(ttsspeed)}")

with open("script.txt", "w") as f:
  f.write(results)
print(results)

if say == "y":
  with wave.open("output.wav", "wb") as wav_file:
    voice.synthesize(str(results), wav_file, length_scale=ttsspeed)


