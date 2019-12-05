# 순위 / 곡 제목 / 가수 (네이버영화 실습과 동일하게 저장)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)

db=client.musics
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# headers = requests.utils.default_headers()
# headers.update({
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
# })
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20191205'
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# geniemusic site html가져와서 parsing
musics = soup.select('table.list-wrap > tbody > tr')
# print(music)
num=0

for music in musics:
    rank = music.select_one('td.number').find(text=True, recursive=False).rstrip()
    artist = music.select_one('td.info > a.artist').text.lstrip()
    title = music.select_one('td.info> a.title').text.lstrip()
    print(rank, artist, title)

    db.musics.insert_one({'rank':num,'artist':artist, 'title':title})

