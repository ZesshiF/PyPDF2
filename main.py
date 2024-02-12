import PyPDF2 as pdf

from PyPDF2 import PdfReader, PdfWriter

file = open("GPT_4_Baker.pdf","rb")
reader = pdf.PdfReader(file)
info = reader.metadata
print("title: ",info.title)
print("author: ", info.author)

pageNumber = len(reader.pages)
print("page:", pageNumber)

for page_number in range(20):  # Change the range to the desired page range
    text_page = reader.pages[page_number].extract_text()
    print(f"\nPage {page_number + 1}:\n{text_page}")

