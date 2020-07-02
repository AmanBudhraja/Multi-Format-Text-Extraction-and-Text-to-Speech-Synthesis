from PIL import Image
from pytesseract import image_to_string
import pyttsx3

x = image_to_string(Image.open('23.png'), lang='eng')
print(x)
engine = pyttsx3.init()
engine.setProperty('rate', 100)
engine.say(x)
engine.runAndWait()