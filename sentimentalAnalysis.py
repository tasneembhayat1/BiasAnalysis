# sentiment library
from textblob import TextBlob


# Textbox for user to input their own text.
input_text = input("Enter some text:")

# Create a TextBlob object
blob = TextBlob(input_text)

# function to calculate sentiment, rating the polarity score
def calculate_sentiment(text):
    """
    Decides whether text is positive, neutral, or negative.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"

# Calling function
sentiment = calculate_sentiment(input_text)

# Print the sentiment of the input text
print("The feeling being protrayed in this text is:", sentiment)
