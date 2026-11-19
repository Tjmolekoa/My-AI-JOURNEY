# Day 2 - Talking to a Real AI Brain (With patience)
import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("My AI Brain is connected!")

topic = input("What do you want to learn about AI today? ")

# Try 5 times, wait a bit each time if Google is busy
for attempt in range(5):
    try:
        print(f"\nTrying to ask the Brain... Attempt {attempt + 1}/5")
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Explain {topic} to me like I am a 10 year old, in 3 short bullet points. Use simple words."
        )
        print("\n--- BRAIN SAYS ---")
        print(response.text)
        break  # It worked; stop trying

    except Exception as e:
        print(f"Google is busy: {e}")
        print("waiting 10 seconds and trying again...")
        time.sleep(10)
else:
    print("\nGoogle is still too busy. Try again in 5 minutes. Your code is correct!")