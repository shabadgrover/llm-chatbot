from app.models.chat_models import ChatRequest, ChatResponse

request = ChatRequest(
    message="Hello"
)

response = ChatResponse(
    response="Hi"
)

print(request)
print(response)