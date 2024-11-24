from flask import Flask, render_template, request
from utils import load_riddles, get_daily_riddle

app = Flask(__name__)

# Load riddles
riddles = load_riddles()
daily_riddle = get_daily_riddle(riddles)

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page to display the riddle and process guesses."""
    message = ""
    show_hint = False  # Flag to track if the hint should be displayed

    if request.method == "POST":
        # Check if the "Show Hint" button was clicked
        if "show_hint" in request.form:
            show_hint = True
        else:
            # Handle answer submission
            user_answer = request.form["answer"].strip().lower()
            correct_answer = daily_riddle["answer"].lower()

            if user_answer == correct_answer:
                message = "🎉 Correct! You solved the riddle!"
            else:
                message = "❌ Incorrect! Try again."

    return render_template(
        "index.html",
        riddle=daily_riddle["riddle"],
        message=message,
        hint=daily_riddle["hint"] if show_hint else ""
    )

if __name__ == "__main__":
    app.run(debug=True)

