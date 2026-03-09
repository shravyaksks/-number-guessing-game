```markdown
# 🎲 Number Guessing Game (Flask)

A fun web-based number guessing game built with **Flask**. The app generates a random number between 1 and 100, and the player tries to guess it. The game tracks attempts and stores history for replay.

---

## 📂 Project Structure
```
guess_num/
│
├── guess_app.py              # Main Flask application
├── data/
│   └── guess_history.json    # Stores past game results
├── static/
│   └── style.css             # Styling for the app
├── templates/
│   ├── guess_index.html      # Game interface
│   └── guess_history.html    # History page
```

---

## 🚀 Features
- Random number between 1–100
- Tracks number of attempts
- Feedback messages: **Too high / Too low / Correct**
- Persistent game history stored in JSON
- Option to reset and play again
- Clean UI with styled forms and tables

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/shravyaksks/guess_num.git
   cd guess_num
   ```

2. **Create a virtual environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the application**
   ```bash
   python guess_app.py
   ```

5. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Screenshots
- **Game Page**: Enter guesses and get feedback.
- **History Page**: View past games with target number and attempts.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS (Jinja2 templates)
- **Data Storage**: JSON file

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📜 License
This project is licensed under the MIT License.
```

---

👉 Save this as `README.md` in your project root, then commit and push:

```bash
git add README.md
git commit -m "Add README.md with project details"
git push
```
