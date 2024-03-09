import pandas as pd
from collections import Counter
import re

# Read the dataset
data = pd.read_csv('data.csv')

# Filter out movies
movies = data[data['type'] == 'Movie']

# Sort the dataset by movie duration in descending order and select the top ten longest movies
top_ten = movies.nlargest(10, 'duration_min')

# Combine the descriptions of the top ten longest movies into a single string
descriptions = ' '.join(top_ten['description'])

# Convert text to lowercase and remove punctuation
descriptions = re.sub(r'[^\w\s]', '', descriptions.lower())

# Split the text into words and count it
word_counts = Counter(descriptions.split())

# Get the 20 most common words
most_common_words = word_counts.most_common(20)

# Print the 20 most common words
print("20 Most Common Words in the Descriptions of Top Ten Longest Movies:")
for word, count in most_common_words:
    print(f"{word}: {count}")
