from pandas import read_csv as csv

data = csv('data.csv')


# 1. How many movie titles mention the  United States?


titles_mentioning_US = data[data['country'].str.contains('United States', na=False)]['title'].count()
print("Number of movie titles mentioning the United States:", titles_mentioning_US)



# 2. How many movie descriptions mention the United States?

description_US = data[data['country'].str.contains('United States', na=False)]['description']
print(description_US.count())


# 3. How many movies are from the United States?

movies_US = data.loc[data['country'] == 'United States', 'show_id'].count()
print(f"There are {movies_US} movies filmed in the United States.")
