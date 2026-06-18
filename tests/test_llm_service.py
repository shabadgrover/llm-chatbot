from app.services.llm_service import LLMService
from langchain_core.messages import HumanMessage

service = LLMService()

messages = [
    HumanMessage(content="Say hello in one sentence.")
]

response = service.get_response(messages)

print(response)