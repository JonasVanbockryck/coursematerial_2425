from collections import namedtuple
Movie = namedtuple('Movie', ['title', 'runtime', 'director', 'actors'])

def actor_count(movie):
    length = len(movie.actors)
    return length

def movies_by(movies, director):
    # return every movie title for a movie (entry in the tuple) in the movies (parameter), if the movie.director (tuple) entry is equal to the director parameter
    return [movie.title for movie in movies if movie.director == director]

def longest_movie(movies):
    if not movies:  # Check if the list is empty
        return None
    
    longest = movies[0]  # Assume the first movie is the longest initially
    for movie in movies[1:]:  # Start checking from the second movie
        if movie.runtime > longest.runtime:
            longest = movie  # Update if we find a movie with a longer runtime
    
    return longest