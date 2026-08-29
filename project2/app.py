import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

X = df[iris.feature_names]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

root = tk.Tk()
root.title("Iris Dataset Classification")
root.geometry("900x700")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Iris Dataset Classification",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)

info_frame = tk.LabelFrame(
    root,
    text="Dataset Information",
    font=("Arial", 13, "bold"),
    padx=15,
    pady=10
)
info_frame.pack(fill="x", padx=25, pady=5)

info_text = (
    f"Dataset Shape: {df.shape}\n"
    f"Classes: Setosa (50) | Versicolor (50) | Virginica (50)\n"
    f"Training Data: {X_train.shape[0]} samples    "
    f"Testing Data: {X_test.shape[0]} samples"
)

tk.Label(
    info_frame,
    text=info_text,
    font=("Arial", 11),
    justify="left"
).pack(anchor="w")

model_frame = tk.LabelFrame(
    root,
    text="Model Evaluation",
    font=("Arial", 13, "bold"),
    padx=15,
    pady=10
)
model_frame.pack(fill="x", padx=25, pady=5)

tk.Label(
    model_frame,
    text=f"Model: Decision Tree Classifier    |    Accuracy: {accuracy * 100:.2f}%",
    font=("Arial", 12, "bold")
).pack()

prediction_frame = tk.LabelFrame(
    root,
    text="New Data Prediction",
    font=("Arial", 13, "bold"),
    padx=20,
    pady=15
)
prediction_frame.pack(fill="x", padx=25, pady=10)

entries = []

for i, feature in enumerate(iris.feature_names):
    label = feature.replace(" (cm)", "").title()
    
    tk.Label(
        prediction_frame,
        text=label + ":",
        font=("Arial", 11)
    ).grid(row=i, column=0, padx=10, pady=6, sticky="w")
    
    entry = ttk.Entry(prediction_frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=6)
    entries.append(entry)

entries[0].insert(0, "5.1")
entries[1].insert(0, "3.5")
entries[2].insert(0, "1.4")
entries[3].insert(0, "0.2")

result_label = tk.Label(
    prediction_frame,
    text="Predicted Species: ---",
    font=("Arial", 13, "bold")
)
result_label.grid(row=0, column=2, rowspan=2, padx=40)

def predict_species():
    try:
        values = [float(entry.get()) for entry in entries]
        
        new_data = pd.DataFrame(
            [values],
            columns=iris.feature_names
        )
        
        prediction = model.predict(new_data)
        species = iris.target_names[prediction[0]]
        
        result_label.config(
            text=f"Predicted Species: {species.upper()}"
        )
        
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )

def show_confusion_matrix():
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation="nearest")
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.xticks(
        range(len(iris.target_names)),
        iris.target_names
    )
    plt.yticks(
        range(len(iris.target_names)),
        iris.target_names
    )
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    
    for i in range(len(cm)):
        for j in range(len(cm)):
            plt.text(
                j,
                i,
                cm[i, j],
                ha="center",
                va="center"
            )
    
    plt.tight_layout()
    plt.show()

def show_classification_plot():
    plt.figure(figsize=(8, 6))
    
    for i, species in enumerate(iris.target_names):
        plt.scatter(
            iris.data[iris.target == i, 0],
            iris.data[iris.target == i, 1],
            label=species
        )
    
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Iris Dataset Classification")
    plt.legend()
    plt.tight_layout()
    plt.show()

def show_report():
    report_window = tk.Toplevel(root)
    report_window.title("Classification Report")
    report_window.geometry("650x400")
    
    tk.Label(
        report_window,
        text="Classification Report",
        font=("Arial", 18, "bold")
    ).pack(pady=15)
    
    text = tk.Text(
        report_window,
        width=70,
        height=15,
        font=("Courier New", 10)
    )
    text.pack(padx=15, pady=10)
    text.insert("1.0", report)
    text.config(state="disabled")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(
    button_frame,
    text="Predict Species",
    command=predict_species
).grid(row=0, column=0, padx=8)

ttk.Button(
    button_frame,
    text="Classification Report",
    command=show_report
).grid(row=0, column=1, padx=8)

ttk.Button(
    button_frame,
    text="Confusion Matrix",
    command=show_confusion_matrix
).grid(row=0, column=2, padx=8)

ttk.Button(
    button_frame,
    text="Classification Plot",
    command=show_classification_plot
).grid(row=0, column=3, padx=8)

root.mainloop()