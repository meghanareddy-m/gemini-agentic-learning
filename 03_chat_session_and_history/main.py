from client_factory import GeminiClientFactory
from pydantic import BaseModel
import json

class Message(BaseModel):
    role:str
    content:str

history : list[Message] =[]

factory = GeminiClientFactory()
client = factory.create_client()

def save_history()->None:

    data = []

    for message in history:
        data.append(message.model_dump())

    with open("conversation_history.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4)

def create_chat():

    return client.chats.create(model="gemini-2.5-flash")


def chat_loop(chat):
    print("Hello!, This is a Gemini Terminal Chat")
    print("Type 'quit' to exit the chat")

    while True:

        user_input = input("You : ")

        if not user_input.strip():
            continue

        if user_input.lower() == "quit":
            save_history()
            print("History Saved")
            print("Bye!")
            break

        history.append(Message(role="user",content=user_input))

        try :
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}\n")
            history.append(Message(role="assistant",content=response.text))

        except Exception as e:
            print(f"Error : {e}")

def main():
    chat = create_chat()
    chat_loop(chat)

if __name__ == "__main__":
    main()
