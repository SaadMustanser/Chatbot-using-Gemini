# -*- coding: utf-8 -*-
"""Chatbot using Gemini API .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1trVdpgTb8FUDq0-2AOFk2doCz85XnqB6

**Installing Google Gemini**
"""

!pip install -q -U google-generativeai

"""**Importing Libraries and connecting to Gemini**"""

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

"""**Importing Key From User Data**"""

# Used to securely store your API key
from google.colab import userdata

"""**Check If key is configured or not**"""

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

"""**Viewing models**"""

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

"""**Using Api and model selection for user Queries and taking User Input**"""

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Using model: {m.name}")
        model = genai.GenerativeModel(m.name)
        break
else:
    raise RuntimeError("No suitable model found.")

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def chat():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        # Generate response from the model
        response_text = get_gemini_response(user_input)
        display(to_markdown(response_text))

if __name__ == "__main__":
    chat()

