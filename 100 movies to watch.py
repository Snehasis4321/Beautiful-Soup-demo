import requests
from bs4 import BeautifulSoup

weblink="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(weblink)
soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())
movies=soup.find_all(name="h3",class_="title")
movies_list=[m.getText() for m in movies]
movies_ordered=movies_list[::-1]
#method 1
# with open("movies.txt",mode="w")as f:
#     for movie in movies_ordered:
#         print(movie)
#         f.write(f"{movie}\n")

# method 2
with open("movies.txt",mode="w")as f:
    for _ in range(len(movies_list) - 1, -1, -1):
        print(movies_list[_])
        f.write(f"{movies_list[_]}\n")