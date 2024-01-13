from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.text)

empireonline_web_page = response.text

soup = BeautifulSoup(empireonline_web_page, "html.parser")
# print(soup.title)

movie_tags = soup.find_all(name="h3")
movie_ranks = []

for tag in movie_tags:
    ranks = tag.getText()
    movie_ranks.append(ranks)

print(movie_ranks)
movies_reverse = movie_ranks[::-1]
print(movies_reverse)



# print(movie_ranks[0].split()[0])
# print(movie_ranks[0].split()[1])
# print(movie_ranks[0].split()[2])

for i in range(0, 100):
    print(movies_reverse[i].split(')'))

with open("movie.txt", mode="w") as file:
    for movie in movies_reverse:
        file.write(f"{movie}\n")