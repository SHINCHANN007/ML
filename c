import google.generativeai as genai
import os
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"

API_KEY = "AIzaSyCm29xP69aObM3S8X1pKOz5SXqs93BuK_c"
extra_API = "AIzaSyBYOI8tV-l4npRGa0z1Y5uF4WxrP4OlnkM"

# Correct way to configure
genai.configure(api_key=API_KEY)

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Ask Gemini a question
response = model.generate_content("Give me Python code to calculate correlation coefficient just give code")

print(response.text)
