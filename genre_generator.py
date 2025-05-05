from google import  genai

client = genai.Client(api_key='')

response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = "what is genre of how long by charlie puth in one word?"
)

print(response.text)