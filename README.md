#  AI Recommendation System

A simple and user-friendly **AI Recommendation System** built with Python. The system recommends movies based on the user's preferred **genre, mood, and interest**.

The project uses a **rule-based recommendation algorithm** that calculates a match score for each movie and displays recommendations according to the user's preferences.

---

##  Project Overview

The AI Recommendation System is designed to provide personalized movie recommendations based on three user preferences:

*  Preferred Genre
*  Preferred Mood
*  Main Interest

Each movie contains predefined categories for genre, mood, and interest. The system compares the user's preferences with the available movie data and calculates a **Match Score out of 100%**.

The project includes both:

* **Command-Line Version** using `main.py`
* **Graphical User Interface (GUI)** using `app.py` and Tkinter

---

##  Features

*  Personalized movie recommendations
*  Genre-based matching
*  Mood-based matching
*  Interest-based matching
*  Match score percentage
*  User-friendly graphical interface
*  Dropdown menus for selecting preferences
*  Validation for missing information
*  Clear button to reset selections and results
*  Built completely with Python
*  Simple and lightweight desktop application

---

##  How the Recommendation System Works

The system uses a simple scoring algorithm.

For every movie:

* Matching genre → **+1 point**
* Matching mood → **+1 point**
* Matching interest → **+1 point**

The maximum score is **3 points**.

The final percentage is calculated using:

```text
Match Score = (Score / 3) × 100
```

For example:

```text
Genre Match     = 1
Mood Match      = 1
Interest Match  = 1

Total Score = 3/3

Match Score = 100%
```

Movies are then sorted from the highest match score to the lowest.

---

##  Available Movies

The system currently contains the following movies:

| Movie                    | Genre             | Mood                   | Interests                     |
| ------------------------ | ----------------- | ---------------------- | ----------------------------- |
| Interstellar             | Sci-Fi, Adventure | Inspiring, Emotional   | Space, Science, Future        |
| The Martian              | Sci-Fi, Adventure | Inspiring, Exciting    | Space, Science, Survival      |
| Inception                | Sci-Fi, Thriller  | Mysterious, Exciting   | Dreams, Mind, Technology      |
| The Pursuit of Happyness | Drama             | Inspiring, Emotional   | Life, Success, Motivation     |
| The Social Network       | Drama             | Interesting, Inspiring | Technology, Business, Success |
| Avengers: Endgame        | Action, Adventure | Exciting, Emotional    | Heroes, Technology, Adventure |

---

##  Graphical User Interface

The GUI version is developed using **Tkinter**, Python's built-in GUI library.

Users can select their:

1. Preferred Genre
2. Preferred Mood
3. Main Interest

After clicking **Get Recommendations**, the application displays the recommended movies with their match percentages.

The **Clear** button resets all selections and results.

---

##  Screenshots

### Screenshot 1

![AI Recommendation System Screenshot 1](screenshots/screenshot1.jpg)

### Screenshot 2

![AI Recommendation System Screenshot 2](screenshots/screenshot2.jpg)


---

##  Project Structure

```text
AI-Recommendation-System/
│
├── main.py
├── app.py
├── README.md
│
└── screenshots/
    ├── screenshot1.jpg
    ├── screenshot2.jpg
    └── screenshot3.jpg
```

---

##  Technologies Used

* **Python**
* **Tkinter**
* **Rule-Based Recommendation Algorithm**

---

##  Requirements

Python 3.x is required to run this project.

Tkinter is included with most standard Python installations on Windows.

No external Python libraries are required.

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Recommendation-System.git
```

### 2. Open the Project Folder

```bash
cd AI-Recommendation-System
```

### 3. Run the Command-Line Version

```bash
python main.py
```

### 4. Run the GUI Version

```bash
python app.py
```

The graphical application will open in a desktop window.

---

##  Command-Line Version

The `main.py` file provides a simple command-line version of the recommendation system.

Users enter their:

* Genre
* Mood
* Interest

The system then displays matching movies along with their match scores.

---

##  GUI Version

The `app.py` file provides a graphical interface built with Tkinter.

It includes:

* Dropdown selection boxes
* Recommendation button
* Clear button
* Results display area
* Input validation
* Match percentage calculation

---

##  Example

If the user selects:

```text
Genre: Sci-Fi
Mood: Inspiring
Interest: Space
```

The system can recommend:

```text
1. Interstellar
   Match Score: 100%

2. The Martian
   Match Score: 100%
```

The recommendations are automatically sorted according to their match scores.

---

##  Future Improvements

Some possible improvements for future versions include:

*  Machine Learning-based recommendations
*  Larger movie database
*  User ratings
*  Movie search functionality
*  Movie posters
*  Favorite movies
*  Saving user preferences
*  Web-based version
*  Database integration
*  More advanced recommendation algorithms

##  Author

**Aima Sadeer**

BS Software Engineering Student


##  Conclusion

The **AI Recommendation System** is a beginner-friendly Python project that demonstrates how user preferences can be used to generate personalized recommendations.

It combines a simple rule-based recommendation algorithm with a graphical interface to create an easy-to-use desktop application.
