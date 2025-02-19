# Intro to Lambda
# Along the way while learning Python, you have probably encountered times when you wished if there was an easier way to write functions, especially the shorter ones - sometimes. If that's the case, you're in luck.

# In Python, lambdas provide a quick way to define small functions. Functions are blocks of reusable code, allowing you to organize your program effectively. They take inputs, perform a task, and return a result. As a beginner, mastering them can open up new possibilities for concise and readable code.

# # The Function With No Name
# Lambda functions (also known as anonymous functions) are concise functions defined without a name. They are often used for short-lived tasks where a full function definition might seem verbose or unneeded.

# The syntax for lambda functions is as follows:

# lambda arguments: expression

# First, we use the reserved lambda keyword to begin defining the function. Then, we can use one or more arguments (separated by commas), followed by a : colon. On the other side of the colon is the expression that may use the arguments to produce an output.

# Here's an example of a regular function that adds numbers, and is assigned to a variable:

# def double(x):
#   return x * 2

# And here's how you can write it as a lambda function:

# double = lambda x: x * 2

# print(double(4))
# # Output: 8

# Although lambda functions are anonymous, they can be assigned to named variables and then used later with the variable name.

# # Use Cases
# Lambdas are particularly useful in situations where a small, one-time-use function is needed.

# When using functions like map() and filter() to perform operations on collections like lists, they require a function as one of their parameters!

# This is where lambda functions come into play:

# numbers = [1, 2, 3, 4, 5]

# tripled_numbers = list(map(lambda x: x * 3, numbers))

# odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

# print(tripled_numbers)  # Output: [3, 6, 9, 12, 15]
# print(odd_numbers)      # Output: [1, 3, 5]

# And just like that, we were able to include a single-line lambda function in each example above. lambda x: x * 2 and also lambda x: x % 2 == 1 really did a lot of work!

# For more information about the functions used:

# map()
# filter()
# GeeksforGeeks map and filter python
# # Practical Examples
# Let's explore a real-world scenario. Suppose you have a list of names, and you want to filter out names that start with the letter 'A':

# names = ['Anthony', 'Benedict', 'Colin', 'Daphne', 'Eloise']

# filtered_names = list(filter(lambda name: name[0].upper() != 'A', names))

# print(filtered_names)   # Output: ['Benedict', 'Colin', 'Daphne', 'Eloise']

# In this example, the lambda function takes in a name argument and returns True if the first character is not 'A' and False otherwise.

# # Using Multiple Arguments
# Lambda can take multiple arguments as well. Here's an example that adds two strings to make a compound word:

# compound_word = lambda str1, str2: str1 + str2

# word = compound_word('fire', 'fly')

# print('The compound word is: {word}')

# We defined a lambda that forms a compound word with two parameters str1 and str2, saved it to a compound_word variable. If we use the compound_variable and give it the arguments 'fire' and 'fly', the word should be 'firefly'! ✨

# Experiment with these concepts, and soon you'll find yourself using Python to tackle a variety of programming challenges. Happy coding!