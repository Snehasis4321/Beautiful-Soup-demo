import requests
from bs4 import BeautifulSoup

# import lxml
#
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'lxml')
# # print(soup.title.string)
# all=soup.find_all(name="a")
# # print(all)
# # for tags in all:
# #     print(tags.getText())
# #
# # heading=soup.find(name="h1",id="name")
# # print(heading)
# name=soup.select_one(selector="#name")
# print(name)
#
response=requests.get("https://news.ycombinator.com/")
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")
article_tags=soup.find_all(name="a",class_="titlelink")
article_texts,article_links=[],[]
for article_tag in article_tags:
    text=article_tag.getText()
    link=article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_votes=[int(score.getText().split(" ")[0]) for score in soup.find_all(name="span",class_="score")]
most_voted=max(article_votes)
print(most_voted)
most_voted_index=article_votes.index(most_voted)

# print(article_texts)
# print(article_links)
# print(article_votes)

print(article_texts[most_voted_index])
print(article_links[most_voted_index])