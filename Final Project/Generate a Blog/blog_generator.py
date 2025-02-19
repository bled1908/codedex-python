# # Generate a Blog with OpenAI 📝

# import openai
# from dotenv import dotenv_values

# config = dotenv_values('.env')

# openai.api_key = config['API_KEY']

# def generate_blog(paragraph_topic):
#   response = openai.completions.create(
#     model = 'gpt-3.5-turbo-instruct',
#     prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
#     max_tokens = 400,
#     temperature = 0.3
#   )
#   retrieve_blog = response.choices[0].text
#   return retrieve_blog

# keep_writing = True

# while keep_writing:
#   answer = input('Write a paragraph? Y for yes, anything else for no. ')
#   if (answer == 'Y'):
#     paragraph_topic = input('What should this paragraph talk about? ')
#     print(generate_blog(paragraph_topic))
#   else:
#     keep_writing = False

# using Google Gemini API
import google.generativeai as genai
from dotenv import dotenv_values
import os

# Change working directory to script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load API key from .env file
config = dotenv_values('.env')
genai.configure(api_key=config['GEMINI_API_KEY'])

def generate_blog(paragraph_topic, previous_content):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Continue writing a blog with the following existing content:\n{previous_content}\n\nNow add a new paragraph about: {paragraph_topic}"
    response = model.generate_content(prompt)
    return response.text if response else "Error generating text."

blog_content = ""  # Store the entire blog content

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no. ')
    if answer.upper() == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ')
        new_paragraph = generate_blog(paragraph_topic, blog_content)
        blog_content += "\n\n" + new_paragraph  # Append new paragraph
        print(new_paragraph)
    else:
        keep_writing = False

print("\nFinal Blog Content:\n", blog_content)
