from client_factory import GeminiClientFactory

factory = GeminiClientFactory()
client=factory.create_client()

def ask_gemini(prompt:str)->str:
    try:
        response = client.models.generate_content(model="gemini-2.5-flash",contents=prompt)

        return response.text
    
    except Exception as e :
        print(f"Generation failed : {e}")
        return ""

def chat_loop():
    print("Hello!, This is a Gemini Terminal Chat")
    print("Type 'quit' to exit the chat")

    while True:

        user_input = input("You : ")

        if user_input.lower() == "quit":
            print("Bye!")
            break

        answer = ask_gemini(user_input)

        print("Gemini: ")
        print(answer)
        print()

if __name__ == "__main__":

    chat_loop()
