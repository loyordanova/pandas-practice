import pandas as pd
from pathlib import Path


# Read paths
ratings_file = Path('/Users/lorayordanova/Downloads/ml-10M100K/ratings.dat')
movies_file = Path('/Users/lorayordanova/Downloads/ml-10M100K/movies.dat')

# Define column names
ratings_columns = ['userId', 'movieId', 'rating', 'timestamp']
movies_columns = ['movieId', 'title', 'genres']

# Read into dataframes
ratings = pd.read_csv(ratings_file, sep='::', names=ratings_columns, engine='python', header=None)
movies = pd.read_csv(movies_file, sep='::', names=movies_columns, engine='python', header=None)

# Join tables on movieiD
movie_lens_df = pd.merge(ratings, movies, on='movieId')

# print(movie_lens_df.head())

# Save to csv
movie_lens_df.to_csv('MovieLens.csv', index=False)

# ----------------------------------------------------------------

# Count rows
data = pd.read_csv('/Users/lorayordanova/PycharmProjects/Indeavr_python_exam/MovieLens.csv')

# print(len(data))

# ----------------------------------------------------------------

# Count how many columns -> you can count the joined columns too
# print(movie_lens_df.shape[1])

# ----------------------------------------------------------------

# Filter the DataFrame to include only rows where the rating is zero and another one where the rating is three
zero_ratings = movie_lens_df[movie_lens_df['rating'] == 0]
three_ratings = movie_lens_df[movie_lens_df['rating'] == 3]

# Count the number of rows with zero/three ratings
# print(len(zero_ratings))
# print(len(three_ratings))

# ----------------------------------------------------------------

# Count the number of unique movies
unique_movies = movie_lens_df['movieId'].nunique()

# print(unique_movies)

# ----------------------------------------------------------------

# Count the number of unique users
unique_users = movie_lens_df['userId'].nunique()

# print(unique_users)

# ----------------------------------------------------------------

# Define the list of genres
selected_genres = ['Drama', 'Comedy', 'Thriller', 'Romance']

# Filter the DataFrame to include only rows with selected genres

"""
Here, the DataFrame movie_lens_df is filtered to include only the rows where the 'genres' column contains 
any of the selected genres. The str.contains() method is used to check if each row's genre contains any of the 
selected genres. The '|'.join(selected_genres) part creates a regular expression pattern that matches any 
of the selected genres.
"""

selected_movies = movie_lens_df[movie_lens_df['genres'].str.contains('|'.join(selected_genres))]

# selected_movies = movie_lens_df[movie_lens_df['genres'].isin(selected_genres)]

# Split genres into separate rows
"""
selected_movies['genres'].str.split('|', expand=True): This part splits the 'genres' column of the selected_movies 
DataFrame into a DataFrame of lists where each list contains the genres for a particular movie. 
The expand=True parameter ensures that the split results are expanded into separate columns.

.stack(): This function is used to pivot the DataFrame. It "stacks" the columns to produce a single-column DataFrame 
with a multi-level index, where the outer level corresponds to the original DataFrame index and the inner level 
corresponds to the position of each element in the lists created by the split operation.

You can achieve a similar result using the explode() function -> Transform each element of a list-like to a row.
genres_split = selected_movies['genres'].str.split('|').explode()

"""
genres_split = selected_movies['genres'].str.split('|', expand=True).stack()

#  Join the split genres back to the main DataFrame

"""
genres_split.reset_index(level=1, drop=True): This part resets the inner level of the multi-level index created by 
stacking the 'genres' column. The level=1 argument specifies that we want to reset the second level of the index 
(since the first level corresponds to the original DataFrame index). The drop=True argument indicates that we want 
to remove the reset index from the DataFrame.

.rename('genre'): This renames the Series resulting from the reset index operation to 'genre'. This step ensures that 
the Series has a meaningful name for better readability.

.to_frame(): This converts the Series into a DataFrame. Since we'll be joining this DataFrame with another DataFrame 
later, converting it to a DataFrame makes the subsequent join operation easier.

.join(selected_movies): This joins the DataFrame containing the split genres with the original selected_movies 
DataFrame. It aligns the rows based on the index, effectively combining the information from both DataFrames.

Overall, this line of code takes the split genres Series, adjusts its structure to prepare it for joining, and then 
joins it with the selected_movies DataFrame to associate the genres with their corresponding movies.

!!!!!!!!!!!!  There is a simple way 
selected_movies_genres = selected_movies.assign(genres=selected_movies['genres'].str.split('|')).explode('genres')
"""
selected_movies_genres = genres_split.reset_index(level=1, drop=True).rename('genre').to_frame().join(selected_movies)

# Count the number of ratings for each genre

"""
.groupby('genre'): This groups the DataFrame by the 'genre' column, meaning that all rows with the same genre 
will be grouped together.

.size(): This function calculates the size of each group, i.e., the number of rows in each group. 
In this context, it counts the number of occurrences of each genre

!!!!!!!! Another way 
ratings_per_genre = selected_movies_genres['genre'].value_counts()

"""
ratings_per_genre = selected_movies_genres.groupby('genre').size()

# print(ratings_per_genre)

# ----------------------------------------------------------------

# Group by movieId and count the number of ratings for each movie
ratings_per_movie = movie_lens_df.groupby('movieId').size()

# Find the movie with the highest number of ratings

"""
ratings_per_movie is a Series containing the number of ratings for each movie, where the movie IDs 
are used as the index.

idxmax() returns the index (in this case, the movie ID) corresponding to the maximum value in the Series.
idxmax() -> Return the row label of the maximum value.
"""
movie_with_highest_ratings = ratings_per_movie.idxmax()

# Get the name of the movie with the highest number of ratings
"""
A boolean mask is a binary array or DataFrame that indicates which elements satisfy a certain condition and which do 
not. It consists of True and False values, where True represents elements that meet the condition and False represents 
elements that do not.

In Pandas, boolean masks are often created by applying conditional expressions to Series or DataFrames.
movies is a DataFrame containing information about movies, including their IDs and titles.
movies['movieId'] == movie_with_highest_ratings creates a boolean mask that is True for the row(s) where the 
movie ID matches movie_with_highest_ratings.
.loc[...] is used to locate the rows based on the boolean mask created above.
['title'] specifies that we want to retrieve the values from the 'title' column of the DataFrame.
.iloc[0] is used to select the first entry (if there are multiple matches, which is unlikely in this case).
"""
highest_rated_movie_name = movies.loc[movies['movieId'] == movie_with_highest_ratings, 'title'].iloc[0]

# print(highest_rated_movie_name)

# ----------------------------------------------------------------

# Count the number of occurrences for each rating
ratings_count = movie_lens_df['rating'].value_counts()

# Get the 5 most given ratings in order from the most to the least
top_5_ratings = ratings_count.head(5)

# print(top_5_ratings)

# ----------------------------------------------------------------

# Count the number of occurrences for each rating

"""
ratings_count is a Series obtained by applying the value_counts() method to the 'rating' column of the 
DataFrame movie_lens_df. This Series contains the count of occurrences for each unique rating value.

The subsequent lines of code retrieve the counts of specific rating values (3, 3.5, and 4) from the ratings_count 
Series using the get() method. If a rating value is not found in the Series, it returns a default value of 0.
"""
ratings_count = movie_lens_df['rating'].value_counts()

# Get the counts of ratings 3, 3.5, and 4
count_3 = ratings_count.get(3, 0)
count_3_5 = ratings_count.get(3.5, 0)
count_4 = ratings_count.get(4, 0)

# Compare the counts
if count_3_5 < count_3 and count_3_5 < count_4:
    print('True')
else:
    print('False')
