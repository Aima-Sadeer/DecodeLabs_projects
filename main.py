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

print("=" * 55)
print("           AI RECOMMENDATION SYSTEM")
print("=" * 55)

print("\nAvailable Genres:")
print("Action | Adventure | Sci-Fi | Thriller | Drama")

print("\nAvailable Moods:")
print("Inspiring | Emotional | Exciting | Mysterious | Interesting")

print("\nAvailable Interests:")
print("Space | Science | Future | Survival | Dreams | Mind")
print("Technology | Life | Success | Motivation | Business")
print("Heroes | Adventure")

genre = input("\nEnter your preferred genre: ").strip().lower()
mood = input("Enter your preferred mood: ").strip().lower()
interest = input("Enter your main interest: ").strip().lower()

user_preferences = {
    "genre": genre,
    "mood": mood,
    "interest": interest
}

recommendations = []

for item in items:
    score = 0

    if user_preferences["genre"] in item["genre"]:
        score += 1

    if user_preferences["mood"] in item["mood"]:
        score += 1

    if user_preferences["interest"] in item["interest"]:
        score += 1

    if score > 0:
        recommendations.append({
            "name": item["name"],
            "score": score
        })

recommendations.sort(key=lambda x: x["score"], reverse=True)

print("\n" + "=" * 55)
print("              RECOMMENDATIONS")
print("=" * 55)

if recommendations:
    for index, recommendation in enumerate(recommendations, start=1):
        percentage = round((recommendation["score"] / 3) * 100)
        print(
            f"{index}. {recommendation['name']} "
            f"- Match Score: {percentage}%"
        )
else:
    print("No matching recommendations found.")

print("\nThank you for using the AI Recommendation System!")