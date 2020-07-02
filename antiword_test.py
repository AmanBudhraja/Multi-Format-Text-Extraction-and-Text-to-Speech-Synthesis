import os, docx2txt, PyPDF2
def get_doc_text(filepath):
    if filepath.endswith('.docx'):
       text = docx2txt.process(filepath)
       return text
    elif filepath.endswith('.doc'):
       # converting .doc to .docx
       doc_file = filepath
       docx_file = filepath + 'x'
       if not os.path.exists(docx_file):
          os.system('antiword ' + doc_file + ' > ' + docx_file)
          with open(docx_file) as f:
             text = f.read()
          os.remove(docx_file) #docx_file was just to read, so deleting
       else:
          # already a file with same name as doc exists having docx extension,
          # which means it is a different file, so we cant read it
          print('Info : file with same name of doc exists having docx extension, so we cant read it')
          text = ''
       return text
    #incomplete below
    elif filepath.endswith('.txt'):
        file1 = open(rfilepath, "r")
        text=file1.read()
        return text
    elif filepath.endswith('.pdf'):
        Pdfobj = open(filepath, "rb")
        PDFread = PyPDF2.PdfFileReader(Pdfobj)
        pageNum = PDFread.numPages
        for i in range(pageNum):
            pageObj = PDFread.getPage(i)
            text = pageObj.extractText()
            if i == 0:
                text1 = text
            else:
                text1 = text1 + text
        return text1



filepath = "A:/ECE9013A_Fall2019.pdf"
text = get_doc_text(filepath)
print(text)
