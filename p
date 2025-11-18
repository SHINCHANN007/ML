$code = @"
import google.generativeai as genai
import os

API_KEY = "YOUR_KEY_HERE"
genai.configure(api_key='AIzaSyBoQlXkv_fXd1j5w_IvNJl1ju_Or_68aIw')

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("here")
print(response.text)
"@

python -c $code
