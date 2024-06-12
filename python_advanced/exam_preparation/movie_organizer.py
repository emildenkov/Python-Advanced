def movie_organizer(*movies):
    movie_collection = {}

    for movie_name, genre in movies:
        if genre not in movie_collection:
            movie_collection[genre] = []
        movie_collection[genre].append(movie_name)

    sorted_movies = dict(sorted(movie_collection.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''

    for g, m in sorted_movies.items():
        sorted_names = sorted(m)
        result += f"{g} - {len(sorted_names)}\n"
        for n in sorted_names:
            result += f"* {n}\n"

    return result.strip()


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
