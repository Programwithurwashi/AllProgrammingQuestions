# importing document from docx
from docx import Document
# make instance of documrnt
doc = Document()
# load text from txt file
with open("text.txt", 'r', encoding='utf-8') as file:
    doc.add_paragraph(file.read())
# save file with any name
doc.save("text.docx")
os.startfile("text.docx")
