import requests

URL = "http://127.0.0.1:8000/chat"

session_id = "session1"

print("Chatbot Started! Type 'exit' to quit.\n")

while True:

    message = input("You: ")

    if message.lower() == "exit":
        print("Goodbye!")
        break

    payload = {
        "message": message
    }

    try:
        response = requests.post(URL, json=payload)

        if response.status_code == 200:
            print("Bot:", response.json()["response"])
        else:
            print("Error:", response.text)

    except Exception as e:
        print("Failed to connect:", str(e))