# import all necessary libraries
from kivy.app import App
from kivymd.theming import ThemeManager
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import num2words
import sys
from PIL import Image
from pytesseract import image_to_string
import pyttsx3
import PyPDF2

# Main program class
class TextSynth(App):
    # Title on the top of the window
    title = "Text Synth"
    
    # To make the color theme of the application dynamic
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGrey'
    theme_cls.accent_palette = 'LightBlue'
    theme_cls.theme_style = 'Light'
    
    # Screen manager variable
    screen_now = ''
    
    # Initialize empty textboxes
    def init_textbox(self):
        self.root.ids.textbox_txt.text = ""
        self.root.ids.textbox_pdf.text = ""
        self.root.ids.textbox_img.text = ""
    
    # To keep track of current screen and revert to previous screen when needed
    def screen_track(self):
        self.screen_now = self.root.ids.screen_manager.current
        return self.screen_now
    
    # Selection of file from file chooser
    def file_selection(self):
        
        # Put file path name into appropriate textfield
        if self.screen_now == 'txt_screen':
            self.root.ids.textfield_txtpath.text = self.root.ids.filechooser.selection[0]
        elif self.screen_now == 'pdf_screen':
            self.root.ids.textfield_pdfpath.text = self.root.ids.filechooser.selection[0]
        elif self.screen_now == 'img_screen':
            self.root.ids.textfield_imgpath.text = self.root.ids.filechooser.selection[0]
       
        # Extract text from TXT
        if self.root.ids.textfield_txtpath.text.endswith('.txt'):
            file1 = open(self.root.ids.textfield_txtpath.text, "r")
            text = file1.read()
            self.root.ids.textbox_txt.text = text
            
        # Extract text from PDF
        elif self.root.ids.textfield_pdfpath.text.endswith('.pdf'):
            Pdfobj = open(self.root.ids.textfield_pdfpath.text, "rb")
            PDFread = PyPDF2.PdfFileReader(Pdfobj)
            pageNum = PDFread.numPages
            for i in range(pageNum):
                pageObj = PDFread.getPage(i)
                text = pageObj.extractText()
                if i == 0:
                    text1 = text
                else:
                    text1 = text1 + text
            self.root.ids.textbox_pdf.text = text1
        
        # Extract text from Image
        elif self.root.ids.textfield_imgpath.text.endswith('.png') or self.root.ids.textfield_imgpath.text.endswith('.jpg'):
            text = image_to_string(Image.open(self.root.ids.textfield_imgpath.text), lang='eng')
            self.root.ids.textbox_img.text = text
            
        else:
            self.root.ids.textbox_txt.text = "Text could not be recognized. Format error..."
            self.root.ids.textbox_pdf.text = "Text could not be recognized. Format error..."
            self.root.ids.textbox_img.text = "Text could not be recognized. Format error..."
    
    def tts(self):
        # Synthesize .txt file
        if self.screen_now == 'txt_screen':
            engine = pyttsx3.init()
            engine.setProperty('rate', 100)
            engine.say(self.root.ids.textbox_txt.text)
            engine.runAndWait()
        # Synthesize .pdf file
        elif self.screen_now == 'pdf_screen':
            engine = pyttsx3.init()
            engine.setProperty('rate', 100)
            engine.say(self.root.ids.textbox_pdf.text)
            engine.runAndWait()
        # Synthesize image files    
        elif self.screen_now == 'img_screen':
            engine = pyttsx3.init()
            engine.setProperty('rate', 100)
            engine.say(self.root.ids.textbox_img.text)
            engine.runAndWait()
    
        
    def exit_app(self):
        sys.exit()
        
    
if __name__ == '__main__':
    TextSynth().run()