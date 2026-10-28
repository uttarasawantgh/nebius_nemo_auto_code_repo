import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("NEBIUS_API_KEY")
base_url = os.getenv("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.com/v1/")

print(f"Loaded Base URL: {base_url}")
print(f"Loaded API Key present: {bool(api_key)} (Length: {len(api_key) if api_key else 0})")

# Initialize OpenAI client pointing directly to Nebius Token Factory
client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

try:
    print("\nSending direct test request to nvidia/nemotron-3-ultra...")
    response = client.chat.completions.create(
        model="nvidia/Nemotron-3-Ultra-550b-a55b",
        messages=[
            {"role": "user", "content": "Hello! Confirm your system status in one sentence."}
        ],
        max_tokens=50,
        temperature=0.1
    )
    
    print("\n[SUCCESS] Direct API Call Completed!")
    print(f"Response Content: {response.choices[0].message.content}")
    print(f"Token Usage Metadata: {response.usage}")

except Exception as e:
    print(f"\n[FAILED] Direct API Call Threw Error: {e}")