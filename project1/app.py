import tkinter as tk
from tkinter import scrolledtext


# -----------------------------
# Chatbot Response Function
# -----------------------------
def get_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hello! How can I help you?"

    elif user_input == "hi":
        return "Hi! Nice to meet you."

    elif user_input == "hey":
        return "Hey! How can I help you?"

    elif user_input == "how are you":
        return "I'm doing great! How about you?"

    elif user_input == "what is your name?":
        return "My name is AI Talkbot."

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    elif user_input == "exit":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


# -----------------------------
# Send Message Function
# -----------------------------
def send_message():
    user_input = message_entry.get().strip()

    if user_input == "":
        return

    # Show user's message
    chat_area.insert(tk.END, "You: " + user_input + "\n")

    # Get chatbot response
    response = get_response(user_input)

    # Show chatbot response
    chat_area.insert(tk.END, "Talkbot: " + response + "\n\n")

    # Clear input box
    message_entry.delete(0, tk.END)

    # Scroll to latest message
    chat_area.see(tk.END)

    # Close software on exit commands
    if user_input.lower() in ["bye", "exit"]:
        root.after(1000, root.destroy)


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("AI Talkbot")
root.geometry("600x650")

# Heading
title_label = tk.Label(
    root,
    text="🤖 AI Talkbot",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=15)

# Chat area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=60,
    height=25,
    font=("Arial", 12)
)
chat_area.pack(padx=15, pady=10)

# Welcome message
chat_area.insert(
    tk.END,
    "Talkbot: Welcome to Rule-Based AI Chatbot!\n"
    "Talkbot: Type 'bye' or 'exit' to end the chat.\n\n"
)

# Bottom frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# Input box
message_entry = tk.Entry(
    bottom_frame,
    width=40,
    font=("Arial", 12)
)
message_entry.pack(side=tk.LEFT, padx=5)

# Send button
send_button = tk.Button(
    bottom_frame,
    text="Send",
    font=("Arial", 12, "bold"),
    command=send_message
)
send_button.pack(side=tk.LEFT, padx=5)

# Press Enter to send message
message_entry.bind("<Return>", lambda event: send_message())

# Start application
root.mainloop()