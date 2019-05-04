import json
import requests
from past.builtins import raw_input
import sys

if len(sys.argv) > 1:
    film_name = str(sys.argv[1])
else:
    sys.exit("缺乏参数电影名称")

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

