from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db=client.naver

app = Flask(__name__)
#app=Flask(__name__, static_url_path='/static' ->경로앞에 static
#app=Flask(__name__, static_folder='static2' -> 경로 앞에 폴더이름이 나오게 지정할 수 있음
#url 루트, ex naver.com/news -> news가 url 루트
@app.route('/')
def home():
    return render_template('index.html')

# @는 mypage()라는 함수의 루트가 mypage이다 라고 꾸며주는 기능
@app.route('/mypage')
def mypage():
    return 'This is mypage'

# ajax와 통신할 API, POST method를 사용
@app.route('/test', methods=['POST'])
def test_post():
    rank_receive = request.form['rank_give']
    rank_receive = int(rank_receive)

    star_receive = request.form['star_give']
    star_receive = float(star_receive)

    print(rank_receive, star_receive)

    db.movies.update_one(
        {'rank':rank_receive},
        {'$set':{'star':star_receive}}
    )
    return jsonify({'result': 'success'})

@app.route('/new', methods = ['POST'])
def new_movie():
    rank_receive = request.form['rank_give']
    if rank_receive is not None:
        rank_receive = int(rank_receive)
    title_receive = request.form['title_give']
    star_receive = request.form['star_give']
    if star_receive is not None:
        star_receive = float(star_receive)

    existing_movie = list(db.movies.find())
    rank = len(existing_movie) + 1

    db.movies.insert_one(
        {'rank':rank, 'title':title_receive, 'star':star_receive}
    )
    return jsonify({'result': 'success'})

# GET method사용, request.args.get 사용, get함수는 url에다가 데이터를 보내기 때문
# @app.route('/test', methods=['GET'])
# def test_get():
#     rank_receive = request.args.get('rank_give')
#     rank_receive = int(rank_receive)
#     movie_info = db.movies.find_one({'rank': rank_receive}, {'_id':0} )
#     return jsonify({
#         'result': 'success',
#         'info': movie_info
#     })

# python이 app.py를 실행 시킬 때 아래줄을 실행시킨다다
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)