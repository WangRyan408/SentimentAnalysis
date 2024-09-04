
from textblob import TextBlob

# Sample text
text = input("Type in a sentence: ")

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment = blob.sentiment

if sentiment.polarity > 0:
  print(f"Positive")
#  print(sentiment.polarity)

elif sentiment.polarity < 0:
  print(f"Negative")
 # print(sentiment.polarity)

else:
  print(f"Neutral")
 # print(sentiment.polarity)
