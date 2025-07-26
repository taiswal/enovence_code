# Scenario 9: Structured Response Generation
# Task: Use the Gemini API to generate a response in JSON format for the query: "List 3 benefits of Python for data science." Handle cases where the response isn’t valid JSON.



import google.generativeai as genai
import json


genai.configure(api_key="YOUR_API_KEY_HERE")  


model = genai.GenerativeModel("gemini-pro")


# user_query = input("Ask Gemini (e.g., List 3 benefits of Python for data science):")
user_query='List 3 benefits of Python for data science'


prompt = f"Give a JSON response with a 'result' key. {user_query}"


response = model.generate_content(prompt)
text_output = response.text.strip()


try:
    data = json.loads(text_output)
    print("JSON Output:")
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print("Not valid JSON. Showing raw response:")
    print(text_output)
