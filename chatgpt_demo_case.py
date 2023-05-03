from ai_case_v2 import OpenAI

ai = OpenAI()

while True:
    prompt = input('User: ')
    if prompt == 'exit':
        break
    response = ai.makeQuery(prompt)
    print('ChatGPT:', response, '(Type "exit" to end the chat)')