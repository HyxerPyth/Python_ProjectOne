import pandas as pd
import math

def actor_info(actor_name, dataset_path='data.csv'):
    data = pd.read_csv(dataset_path)

    # Convert actor_name to lowercase
    actor_name = actor_name.lower()

    # Drop rows with missing values in the 'cast' column
    data = data.dropna(subset=['cast'])

    # Filter the dataset for rows containing the actor's name in the 'cast' column
    actor_movies = data[data['cast'].str.lower().str.contains(actor_name)]

    if actor_movies.empty:
        return f"No movie found for the artist: {actor_name.capitalize()}"

    # Calculate the average movie duration 
    avg_duration = math.ceil(actor_movies['duration_min'].mean())

    # Get a list of the actor's movies
    movies_list = actor_movies[['title', 'duration_min']].values.tolist()

    return avg_duration, movies_list

