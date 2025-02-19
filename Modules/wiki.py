# # Python Packages
# Modules are the .py files that contain definitions for functions, classes, and variables. Packages are the folders that contain the modules.

# So far, we have been working with singular modules (i.e., bday_messages.py). However, a collection of related modules with a similar purpose is a package.

# This is where things get crazy. There are 400,000+ Python packages in the world (and that's only counting those on PyPI, the official Python Package Index). You could even build and register your own module on PyPI for others to use!

# Python can tell a regular folder from a package if it has an __init__.py file, in addition to other .py files.

# Note: Some large and specialized packages are called "libraries".

# Here are some examples of packages and libraries in Python:

# 🔢 NumPy, Pandas, SciPy for data analysis.
# 📊 Matplotlib, Seaborn, Plotly for data visualization.
# 🧠 Scikit-learn, TensorFlow for machine learning.
# 🌐 Beautiful Soup for web scraping.
# 👾 Pygame for mini-games.
# 🤖 NLTK, OpenAI for chatbots.
# 🛠️ OS, Requests for automation.
# These packages make Python one of the most versatile languages in existence; you can use it to make all sorts of applications!

# # Installing with pip3
# While this isn't the only package installer, pip is a popular one!

# Note: Installing modules, packages, and libraries is currently not possible with our online editor on the right. To follow along, an external editor like VS Code or a command prompt/terminal will be needed.

# Installing packages with pip can be done in the terminal. For example, to download a popular data plotting library called Matplotlib:

# pip3 install matplotlib

# If this command doesn't work or you get a "not found" error, try running pip install matplotlib.

# Note: pip3 is typically used when working with Python 3. It's an updated version of the old pip, which was mainly for Python 2 (retired in 2020).

# The package can then be imported in a Python file, like so:

# import matplotlib

# And then to access the various modules, functions, and other tools, we use . dot notation. For example, we can now use Matplotlib's plotly module:

# import matplotlib.plotly

# Instructions
# Note: For this exercise, an outside code editor is needed. We recommend using VS Code. Check out this article to get started.

# It's time to try out a Python package!

# First, make sure pip is installed by running pip3 in a terminal. If not, follow the steps to do so here.

# Next, install a package called wikipedia.

# pip3 install wikipedia

# Next, create a new file called wiki.py.

# Then, use the wikipedia package's documentation to search for a phrase of your choice.

# A few examples could be:

# "Philosophy of life"
# "Python (programming language)"
# "Galaxy"
# Try running this program in the terminal with:

# python3 wiki.py -use python if python 3 is not working

import wikipedia

print(wikipedia.summary("Python (programming language)"))
# also can use wikipedia.search("Python (programming language)") to get the search results