from flask import Flask, render_template, request
from sentiment import analyze_sentiment
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)

        conn = sqlite3.connect("sentiment.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO history (text, sentiment) VALUES (?, ?)", (text, result))
        conn.commit()
        conn.close()

    return render_template("index.html", result=result)

@app.route("/history")
def history():
    conn = sqlite3.connect("sentiment.db")
    cur = conn.cursor()

    cur.execute("SELECT text, sentiment FROM history")
    data = cur.fetchall()

    counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for _, s in data:
        counts[s] += 1

    conn.close()
    return render_template("history.html", history=data, counts=counts)

if __name__ == "__main__":
    app.run(debug=True)
