from flask import Flask, render_template, request, session, redirect, url_for
import random, os, json

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session

DATA_FILE = "data/guess_history.json"
os.makedirs("data", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def game():
    # Initialize game if not started
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0
        session["finished"] = False

    message = None

    if request.method == "POST" and not session["finished"]:
        guess = int(request.form["guess"])
        session["attempts"] += 1

        if guess < session["number"]:
            message = "Too low!"
        elif guess > session["number"]:
            message = "Too high!"
        else:
            message = f"Correct! You guessed it in {session['attempts']} attempts."
            session["finished"] = True

            # Save game result
            entry = {
                "number": session["number"],
                "attempts": session["attempts"]
            }
            with open(DATA_FILE, "a") as f:
                f.write(json.dumps(entry) + "\n")

    return render_template("guess_index.html", message=message, finished=session["finished"])

@app.route("/reset")
def reset():
    session.pop("number", None)
    session.pop("attempts", None)
    session.pop("finished", None)
    return redirect(url_for("game"))

@app.route("/history")
def history():
    games = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                games.append(json.loads(line.strip()))
    return render_template("guess_history.html", games=games)

if __name__ == "__main__":
    app.run(debug=True)
