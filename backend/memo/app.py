from flask import Flask, render_template, request, jsonify
import requests as req
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.sparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# client는 url, comment 보낸다
# url로 스크래핑, html가져와서 meta 태그 파싱 >og태그 파싱
@app.route('/post', methods = ['POST'])
def save_post():
    try:
        url_receive =  request.form['url_give']
        comment_receive = request.form['comment_give']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }

        source = req.get(url_receive, headers=headers)
        soup = BeautifulSoup(source.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        url_image = og_image['content']
        url_title = og_title['content']
        url_description = og_description['content']

        article = {
            'title' : url_title,
            'description' : url_description,
            'image' : url_image,
            'url' : url_receive,
            'comment' : comment_receive
        }
        db.articles.insert_one(article)

    except Exception as e:
        print(e)
        return jsonify({'result':'fail'})
        # jsonify는 python dictionary를 json response로 바꿔주는 Flask 내장함수
        # url_image = og_image['content']
        # url_title = og_title['content']
        # url_description = og_description['content']

    return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def list_articles():
    try:
        articles = list(db.articles.find({}, {'_id':0}))
    except Exception as e:
        print(e)
        return jsonify({'result':'fail'})

    return jsonify({
        'articles' : articles,
        'result' : 'success'
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)

#0.0.0.0 => 모든 로컬 ip 주소를 허용한다는 의미
