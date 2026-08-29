print("Welcome to Rule-Based AI Chatbot")
print("Type 'bye' or 'exit' to end the chat.")

while True:

    user_input = input("You: ")

    if user_input == "hello":
        print("Talkbot: Hello! How can I help you?")

    elif user_input == "hi":
        print("Talkbot: Hi! Nice to meet you.")

    elif user_input == "hey":
        print("Talkbot: Hey! How can I help you?")   

    elif user_input == "how are you":
        print("I'm doing great! How about you?")

    elif user_input == "What is your name?":
        print("MY name is AI Talkbot")   

    elif user_input == "bye":
        print("Talkbot: Goodbye! Have a nice day.")
        break

    elif user_input == "exit":
        print("Talkbot: Goodbye! Have a nice day.")
        break

    else:
        print("Talkbot: Sorry, I don't understand that.")