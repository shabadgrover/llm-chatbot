from app.services.llm_service import LLMService
from app.services.masking_service import mask_pii

from langchain_core.messages import HumanMessage, AIMessage

from app.utils.logger import get_logger


class ChatService:

    def __init__(self):
        self.llm_service = LLMService()
        self.chat_history = []

        self.logger = get_logger()

    def chat(self, message):

        self.logger.info("Request received")

        masked_message = mask_pii(message)

        self.logger.info("Message masked")

        self.chat_history.append(
            HumanMessage(content=masked_message)
        )

        self.logger.info("LLM request sent")

        try:
            response = self.llm_service.get_response(
                self.chat_history
            )

            self.logger.info("Response generated")

        except Exception as e:
            self.logger.error(
                f"Failed to generate response: {str(e)}"
            )

            raise

        self.chat_history.append(
            AIMessage(content=response)
        )

        return response