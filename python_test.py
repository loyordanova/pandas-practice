"""
Without using pandas, you can still achieve similar functionality, but it would require more low-level
file handling and data manipulation. Here's a simplified version of the code without pandas:
"""

from pathlib import Path

# Read paths
ratings_file = '/Users/lorayordanova/Downloads/ml-10M100K/ratings.dat'
movies_file = '/Users/lorayordanova/Downloads/ml-10M100K/movies.dat'

# Define data structures to store data
ratings_data = []
movies_data = []

# Read ratings data
with open(ratings_file, 'r') as file:
    for line in file:
        userId, movieId, rating, timestamp = line.strip().split('::')
        ratings_data.append({'userId': int(userId), 'movieId': int(movieId), 'rating': float(rating), 'timestamp': int(timestamp)})

# Read movies data
with open(movies_file, 'r') as file:
    for line in file:
        movieId, title, genres = line.strip().split('::')
        movies_data.append({'movieId': int(movieId), 'title': title, 'genres': genres})

# Join tables on movieID
movie_lens_data = []
for rating in ratings_data:
    for movie in movies_data:
        if rating['movieId'] == movie['movieId']:
            movie_lens_data.append({**rating, **movie})

# Save to CSV
with open('MovieLens.csv', 'w') as file:
    file.write('userId,movieId,rating,timestamp,title,genres\n')
    for entry in movie_lens_data:
        file.write(f"{entry['userId']},{entry['movieId']},{entry['rating']},{entry['timestamp']},{entry['title']},{entry['genres']}\n")

# Count rows
with open('MovieLens.csv', 'r') as file:
    num_rows = sum(1 for _ in file)
print(num_rows)

# Count columns
with open('MovieLens.csv', 'r') as file:
    first_line = file.readline().strip()
    num_columns = len(first_line.split(','))
print(num_columns)

# Filter data
zero_ratings = [entry for entry in movie_lens_data if entry['rating'] == 0]
three_ratings = [entry for entry in movie_lens_data if entry['rating'] == 3]
print(len(zero_ratings))
print(len(three_ratings))

# Count unique movies and users
unique_movies = len(set(entry['movieId'] for entry in movie_lens_data))
unique_users = len(set(entry['userId'] for entry in movie_lens_data))
print(unique_movies)
print(unique_users)

# Define selected genres
selected_genres = ['Drama', 'Comedy', 'Thriller', 'Romance']

# Filter data based on selected genres
selected_movies = [entry for entry in movie_lens_data if any(genre in entry['genres'] for genre in selected_genres)]
print(len(selected_movies))

# Count ratings per genre
genre_counts = {}
for movie in selected_movies:
    for genre in movie['genres'].split('|'):
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
print(genre_counts)

# Find movie with highest ratings
ratings_per_movie = {}
for entry in movie_lens_data:
    ratings_per_movie[entry['movieId']] = ratings_per_movie.get(entry['movieId'], 0) + 1
movie_with_highest_ratings = max(ratings_per_movie, key=ratings_per_movie.get)
highest_rated_movie_name = next((movie['title'] for movie in movies_data if movie['movieId'] == movie_with_highest_ratings), None)
print(highest_rated_movie_name)

# Count ratings
ratings_count = {}
for entry in movie_lens_data:
    rating = entry['rating']
    ratings_count[rating] = ratings_count.get(rating, 0) + 1

count_3 = ratings_count.get(3, 0)
count_3_5 = ratings_count.get(3.5, 0)
count_4 = ratings_count.get(4, 0)
if count_3_5 < count_3 and count_3_5 < count_4:
    print('True')
else:
    print('False')
