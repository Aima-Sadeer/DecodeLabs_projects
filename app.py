import tkinter as tk
from tkinter import ttk, messagebox

items = [
    {
        "name": "Interstellar",
        "genre": ["sci-fi", "adventure"],
        "mood": ["inspiring", "emotional"],
        "interest": ["space", "science", "future"]
    },
    {
        "name": "The Martian",
        "genre": ["sci-fi", "adventure"],
        "mood": ["inspiring", "exciting"],
        "interest": ["space", "science", "survival"]
    },
    {
        "name": "Inception",
        "genre": ["sci-fi", "thriller"],
        "mood": ["mysterious", "exciting"],
        "interest": ["dreams", "mind", "technology"]
    },
    {
        "name": "The Pursuit of Happyness",
        "genre": ["drama"],
        "mood": ["inspiring", "emotional"],
        "interest": ["life", "success", "motivation"]
    },
    {
        "name": "The Social Network",
        "genre": ["drama"],
        "mood": ["interesting", "inspiring"],
        "interest": ["technology", "business", "success"]
    },
    {
        "name": "Avengers: Endgame",
        "genre": ["action", "adventure"],
        "mood": ["exciting", "emotional"],
        "interest": ["heroes", "technology", "adventure"]
    }
]

def get_recommendations():
    genre = genre_var.get().lower()
    mood = mood_var.get().lower()
    interest = interest_var.get().lower()

    if not genre or not mood or not interest:
        messagebox.showwarning(
            "Missing Information",
            "Please select your genre, mood, and interest."
        )
        return

    recommendations = []

    for item in items:
        score = 0

        if genre in item["genre"]:
            score += 1

        if mood in item["mood"]:
            score += 1

        if interest in item["interest"]:
            score += 1

        if score > 0:
            recommendations.append(
                (item["name"], score)
            )

    recommendations.sort(key=lambda x: x[1], reverse=True)

    result_text.delete("1.0", tk.END)

    if recommendations:
        result_text.insert(
            tk.END,
            "RECOMMENDED ITEMS\n\n"
        )

        for index, (name, score) in enumerate(
            recommendations, start=1
        ):
            percentage = round((score / 3) * 100)

            result_text.insert(
                tk.END,
                f"{index}. {name}\n"
                f"   Match Score: {percentage}%\n\n"
            )
    else:
        result_text.insert(
            tk.END,
            "No matching recommendations found."
        )

def clear_results():
    genre_var.set("")
    mood_var.set("")
    interest_var.set("")
    result_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("AI Recommendation System")
root.geometry("700x650")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="AI Recommendation System",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=(25, 5))

subtitle_label = tk.Label(
    root,
    text="Enter your preferences to get personalized recommendations",
    font=("Arial", 11)
)
subtitle_label.pack(pady=(0, 25))

input_frame = tk.Frame(root)
input_frame.pack()

genre_var = tk.StringVar()
mood_var = tk.StringVar()
interest_var = tk.StringVar()

tk.Label(
    input_frame,
    text="Preferred Genre",
    font=("Arial", 11, "bold")
).grid(row=0, column=0, padx=15, pady=10, sticky="w")

genre_box = ttk.Combobox(
    input_frame,
    textvariable=genre_var,
    values=[
        "Action",
        "Adventure",
        "Sci-Fi",
        "Thriller",
        "Drama"
    ],
    state="readonly",
    width=30
)
genre_box.grid(row=0, column=1, padx=15, pady=10)

tk.Label(
    input_frame,
    text="Preferred Mood",
    font=("Arial", 11, "bold")
).grid(row=1, column=0, padx=15, pady=10, sticky="w")

mood_box = ttk.Combobox(
    input_frame,
    textvariable=mood_var,
    values=[
        "Inspiring",
        "Emotional",
        "Exciting",
        "Mysterious",
        "Interesting"
    ],
    state="readonly",
    width=30
)
mood_box.grid(row=1, column=1, padx=15, pady=10)

tk.Label(
    input_frame,
    text="Main Interest",
    font=("Arial", 11, "bold")
).grid(row=2, column=0, padx=15, pady=10, sticky="w")

interest_box = ttk.Combobox(
    input_frame,
    textvariable=interest_var,
    values=[
        "Space",
        "Science",
        "Future",
        "Survival",
        "Dreams",
        "Mind",
        "Technology",
        "Life",
        "Success",
        "Motivation",
        "Business",
        "Heroes",
        "Adventure"
    ],
    state="readonly",
    width=30
)
interest_box.grid(row=2, column=1, padx=15, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=25)

recommend_button = tk.Button(
    button_frame,
    text="Get Recommendations",
    command=get_recommendations,
    font=("Arial", 11, "bold"),
    width=22,
    height=2
)
recommend_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_results,
    font=("Arial", 11, "bold"),
    width=12,
    height=2
)
clear_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(
    root,
    text="Recommendations",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=(5, 10))

result_text = tk.Text(
    root,
    width=65,
    height=14,
    font=("Arial", 11),
    wrap=tk.WORD
)
result_text.pack()

root.mainloop()