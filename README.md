# The Legend of Python - Beginner

## 📌 Overview
Welcome to **The Legend of Python - Beginner**! This repository is designed to help beginners learn Python through hands-on projects, exercises, and a final project.

## 📁 Project Structure
```
The-Legend-Of-Python/
│── .git/                     # Git repository files
│── .gitignore                # Git ignore file
│── .vscode/                  # VS Code settings
│── Classes and Objects/      # Object-Oriented Programming concepts
│── Control Flow/             # Conditional statements and loops
│── Final Project/            # Hands-on projects
│   │── Build a Discord Bot/   # Creating a Discord bot
│   │   │── bot.py             # Main bot script
│   │   │── .env               # Environment variables (not tracked)
│   │── Create GIF/            # Generating GIFs using Python
│   │   │── create_gif.py   # Script to create GIFs
│   │── Generate a Blog/       # Automating blog generation
│   │   │── blog_generator.py  # Script for blog creation
│── Functions/                # Function definitions and usage
│── Hello World/              # First Python script
│── Lists/                    # Working with lists in Python
│── Loops/                    # Looping structures in Python
│── Modules/                  # Importing and using modules
│── Variables/                # Variables and data types
│── Project_terminal_adventure.py # Terminal-based adventure game
│── README.md                 # Project documentation
```

## 🚀 Getting Started
### Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Git

### Setup Instructions
1. **Clone the Repository**
   ```sh
   git clone https://github.com/bled1908/codedex-python.git
   ```
2. **Navigate to the Project Directory**
   ```sh
   cd The-Legend-Of-Python
   ```
3. **Create a Virtual Environment** (Recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
4. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## 🎯 Final Project - Hands-on Python Applications
### 1️⃣ Build a Discord Bot
1. **Create a `.env` file** and add your bot token:
   ```
   DISCORD_BOT_TOKEN=your_token_here
   ```
2. **Run the bot**
   ```sh
   python Final Project/Build a Discord Bot/bot.py
   ```

### 2️⃣ Create GIFs
1. **Run the GIF generator script**
   ```sh
   python Final Project/Create GIF/gif_generator.py
   ```

### 3️⃣ Generate a Blog
1. **Run the blog generator script**
   ```sh
   python Final Project/Generate a Blog/blog_generator.py
   ```

## ⚠️ Important Notes
- **Secrets Management:** `.env` files should NOT be pushed to GitHub.
- **Git Best Practices:** Make sure `.gitignore` includes `.env` to avoid accidental leaks.

## 📜 License
This project is open-source under the [MIT License](LICENSE).

## 🤝 Contributing
Feel free to fork this repo, make improvements, and submit pull requests!

---
Happy coding! 🎉