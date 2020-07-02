# Introduction
Optical character recognition or OCR basically convert text in an image into a form that a
computer can manipulate easily. An OCR system helps one to take a book or a magazine and
feed it directly to an electronic computer file, which then can be edited using a word or PDF
editors. The system for OCR usually includes an optical scanner for reading the text and a
complex software to analyse the images. But the issue with this type of OCR system is that
they are only capable of converting images of text to text file only.

# Problem definition and motivation
This project analyses the extracted file further and convert it into an audio file.
Most of the text files that are available online nowadays cannot be read or understood by a lot
of people. For example, people who are visually impaired cannot read these text file. So, we
want to create an application which can not only extract text from images but is also capable
of saving it into multiple formats so that it can be accessed by everyone.

# Methodology
We start by extracting the text and graphic elements and scanning the image then convert it
into a matrix of black and white dots called bitmap. Then we enhance the accuracy of the
process by adjusting the brightness and contrast of the image. Next we split the image into
zones to identify the areas of interest like where the images or the texts are present which
initiates the extraction process. The text is then further broken down into lines words and
characters. The software then matches the characters through comparison and various
detection algorithms. Finally, we get the text from the image that we are given. This process
is not one hundred percent accurate and may require correction in some elements that are not
scanned correctly.
The text data is analysed by the speech synthesizer and then converted to recorded speech
using the text-to-speech technology. This technology mainly has three stages text analysis,
processing, and wave form generation.

# Deliverables
Final application will include the following functionalities: -
Extracting text from images and converting it to text file like PDF or word
Creating an audio file from a text file
Libraries used: - PyTesseract, pyttsx3
Hardware required: - a web cam or mobile camera for taking pictures
Data required: - Images with textGroup number 8

Contributors - Aman Budhraja, Heena Shrestha, Mashruk Kabir, Urvashi Gupta 
