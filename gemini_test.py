import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyAm34W4HZbjIzM8G0MsTbDbQ5lJVcvc5cU")

# Use a valid model name from your list
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate content
response = model.generate_content("Explain AI in simple words")

print(response.text)