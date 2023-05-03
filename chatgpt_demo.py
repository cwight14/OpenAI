#import the openai package and your own key saved as a string in a separate file.
import openai
from secret import OPEN_API_KEY

#call the api_key function from openai and define this as your key. Define the LLM you want to use.
openai.api_key = OPEN_API_KEY
model_id = 'gpt-3.5-turbo'

#define the function 
def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []
conversation.append({'role': 'system', 'content': 'How may I help you?'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n (Type "exit" to end the chat)'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

#
while True:
    prompt = input('User:')
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
    if prompt.strip().lower() == 'exit':
        break