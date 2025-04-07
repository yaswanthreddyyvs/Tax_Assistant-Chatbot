import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyAPLYMq4Ls7dkCeM4RZG7tY77TS3AvtlHM")  # Replace with your actual API key

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(message):
    message = message.lower()  # Make the message lowercase for easier matching

    # Pre-programmed answers for common tax questions
    if "income tax" in message:
        return "Income tax is a tax on your earnings, like salary or business profits. It’s collected by the government."
    elif "tax slabs" in message:
        return "For FY 2023-24 (India), the new tax regime has slabs like: 0-3L (0%), 3-6L (5%), 6-9L (10%), and so on."
    elif "file tax" in message:
        return "You can file taxes online at https://www.incometax.gov.in with your PAN card. Need steps?"
    elif "pan card" in message:
        return "A PAN card is a 10-digit ID issued by India’s Income Tax Department for tax purposes."
    elif "hello" in message or "hi" in message:
        return "Hey there! I’m TaxBot, your tax helper. What’s your tax question?"

    # Use Gemini AI for questions not covered by pre-programmed answers
    try:
        response = model.generate_content(
            f"You are a tax assistant. Answer tax-related questions clearly and concisely, focusing on general information, not personalized advice. Question: {message}"
        )
        return response.text.strip()
    except Exception as e:
        return f"Oops, I’m having trouble with Gemini AI: {str(e)}. Try asking something else about taxes!"