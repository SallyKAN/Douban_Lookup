import json
import requests
from past.builtins import raw_input

film_name = raw_input()
movie_search_url = "https://api.douban.com/v2/movie/search?q=" + film_name
content = requests.get(movie_search_url).text
res = json.loads(content)['subjects'][0]
name = res['title']
original_title = res['original_title']
casts = res['casts']
directors = res['directors']
rating = res['rating']['average']
print()
print("name:" + name + "/" +original_title)
print("rate:" + str(rating))
print("directors:" + '  '.join(str(director['name']) for director in directors))
print("casts:" + '  '.join(str(cast['name']) for cast in casts))
# print("country:" + country)
# print("duration:" + movie_duration)
# print("pubdate:" + pubdate)
# print("country:" + movie_type[0] +"\\\\"+ movie_type[1] +"\\\\"+ movie_type[2])
# print("--------------------------------------------------------By Douban")
# 该片段来自于http://outofmemory.cn
