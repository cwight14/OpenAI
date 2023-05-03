import openai
from secret import OPEN_API_KEY

class OpenAI:
    # Add class variable to store conversation history
    conversation = []

    def __init__(self):
        openai.api_key = OPEN_API_KEY
        self.model_id = 'gpt-3.5-turbo'

    def ChatGPT_conversation(self, conversation):
        response = openai.ChatCompletion.create(
            model=self.model_id,
            messages=conversation
        )
        # Append the system response to the conversation history
        self.conversation.append({'role': 'system', 'content': response.choices[0].text.strip()})
        # Return the system response
        return response.choices[0].text.strip()

    def makeQuery(self, initial_prompt):
        # Add the initial user prompt to the conversation history
        self.conversation.append({'role': 'user', 'content': initial_prompt})
        # Call ChatGPT_conversation method with the stored conversation history
        response = self.ChatGPT_conversation(self.conversation)
        # Return the final system response
        return response.strip()
