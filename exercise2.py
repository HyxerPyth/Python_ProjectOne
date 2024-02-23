from pandas import read_csv as csv

data = csv('data.csv')

def movie_info (name): 
    director_match = data[data['director'].str.contains(name, na=False)]['title'].count()
    if director_match > 0:
        return (
            f"There are {director_match} directors named {name} in this dataset."
        )
    else: 
        return(
            f"No directors were found with the name: {name}"
        )

users_input = str(input("Type the name of the director: "))

print(movie_info(users_input))