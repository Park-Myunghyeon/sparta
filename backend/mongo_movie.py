from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.naver

a =db.movies.find_one({'title':'사운드 오브 뮤직'})
print(a['star'])

movie = list(db.movies.find({'star':a['star']}))
movie_list=[]
for m in movie:
    b= m['title']
    movie_list.append(b)

db.movies.update_many({'star':a['star']}, {'$set':{'star':0}})
zero = list(db.movies.find({'star':0}))
for z in zero:
    print(z['title'],z['star'])
print(movie_list)

movies = db.movies.find()
for movi in movies:
    db.movies.update_one(
        {'title':movi['title']},
        {'$set':{'star':float(movi['star'])}}
    )

new_movies = list(
    db.movies.find({'star': {'$gte':9.45, '$lt':9.7}}) #gte는 greater than equal, lte는 less than equal
)
print(new_movies)
print(len(new_movies))
