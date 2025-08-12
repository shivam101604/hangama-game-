# Create folder and navigate into it
mkdir hangman-game
cd hangman-game

# Create the Python file
nano hangman.py
# (Paste the code and save with Ctrl+O, Enter, Ctrl+X)

# Initialize Git and push
git init
git add hangman.py
git commit -m "Initial commit - Hangman Game"
git branch -M main

# Replace with your GitHub repo URL
git remote add origin https://github.com/yourusername/hangman-game.git
git push -u origin main
