from app.services.chat_service import ChatService

chat_service = ChatService()

response = chat_service.chat(
    "My name is Shabad"
)

print(response)

response = chat_service.chat(
    "What is my name?"
)

print(response)