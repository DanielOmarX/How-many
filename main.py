from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def count_words(text):
  """
  This function counts the number of words in a given text.

  Args:
      text: The text to count the words in.

  Returns:
      The number of words in the text.
  """
  # Split the text into words by whitespace characters.
  words = text.split()
  # Return the number of words.
  return len(words)

# Get user input
text = input("Enter your text: ")

# Count and print the number of words
number_of_words = count_words(text)
print(f"The number of words in your text is: {number_of_words}")
