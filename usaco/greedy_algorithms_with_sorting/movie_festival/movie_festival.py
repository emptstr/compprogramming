def sort_movies(m):
    return m[1]

num_movies = int(input())
movies = [list(map(int, input().split())) for _ in range(num_movies)]

movies.sort(key=sort_movies)
movies_watched = 1
last_end_time = movies[0][1]
for i in range(1, num_movies):
    next_movie = movies[i]
    if next_movie[0] >= last_end_time:
        last_end_time = next_movie[1]
        movies_watched+=1

print(movies_watched)
