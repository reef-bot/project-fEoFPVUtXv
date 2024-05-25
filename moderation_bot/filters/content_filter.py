# content_filter.py

# Import necessary libraries
import re

# Define a function to filter inappropriate content
def filter_content(message):
    # List of inappropriate words or phrases
    inappropriate_words = ["bad_word1", "bad_word2", "bad_phrase1"]

    # Check if message contains any inappropriate words
    for word in inappropriate_words:
        if re.search(r"\b" + re.escape(word) + r"\b", message, re.IGNORECASE):
            return True

    return False

# Define a function to censor inappropriate content
def censor_content(message):
    # List of inappropriate words or phrases
    inappropriate_words = ["bad_word1", "bad_word2", "bad_phrase1"]

    # Censor inappropriate words in the message
    for word in inappropriate_words:
        message = re.sub(r"\b" + re.escape(word) + r"\b", "*censored*", message, flags=re.IGNORECASE)

    return message