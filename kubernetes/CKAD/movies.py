# URI # 5
# Gully Boy # 5
# Badla # 5
# Kabir Singh # 5
# THE END

data = input()
res = {}
while (data != 'THE END'):
    movie,rating = data.split("#")
    movie,rating = movie.strip(),int(rating.strip())
    res[movie] = res.get(movie,0)+rating
    data = input()

hrating = 0
movieName = ''

for movie,rating in res.items():
    temp = rating
    if hrating < temp:
        hrating = temp
        movieName = movie

for movie,rating in res.items():
    # temp = rating
    if hrating == rating:
        if movie.upper() < movieName.upper():
            hrating = rating
            movieName = movie
print(movieName,rating)