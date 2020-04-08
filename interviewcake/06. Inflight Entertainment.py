def there_are_complement_movies(flight_duration, movie_lengths):
    movie_complements = set()
    for movie_length in movie_lengths:
        if movie_length >= flight_duration:
            continue
        complement = flight_duration - movie_length
        if complement in movie_complements:
            return True
        movie_complements.add(movie_length)
    return False


print(there_are_complement_movies(10, [5, 5]))  # True
print(there_are_complement_movies(10, [6, 1, 4]))  # True
print(there_are_complement_movies(10, [7, 3]))  # True
print(there_are_complement_movies(10, [7, 2]))  # False
print(there_are_complement_movies(10, [3, 1, 2]))  # False
print(there_are_complement_movies(4, [100, 3, 1]))  # True
