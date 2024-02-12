import openai
import PyPDF2 as pdf

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

file = open("GPT_4_Baker.pdf", "rb")
reader = pdf.PdfReader(file)
info = reader.metadata
print("title: ", info.title)
print("author: ", info.author)

pageNumber = len(reader.pages)
print("page:", pageNumber)

# Initialize variables to store extracted information
project_name = ""
author = ""
members_students_ids = ""
advisor = ""
conclusion = ""

for page_number in range(20):  # Change the range to the desired page range
    text_page = reader.pages[page_number].extract_text()
    print(f"\nPage {page_number + 1}:\n{text_page}")


# Construct the prompt for summarization
prompt = f"Summarize the information extracted from the PDF:\n\nProject Name: {project_name}\nAuthor: {author}\nMembers and Student IDs: {members_students_ids}\nAdvisor: {advisor}\nConclusion: {conclusion}"

# Use OpenAI API to generate response for the prompt
response = openai.Completion.create(
    engine="text-davinci-002",  # You can use a different engine if needed
    prompt=prompt,
    max_tokens=200  # Adjust the max tokens based on your desired response length
)

generated_response = response.choices[0].text.strip()
print(generated_response)