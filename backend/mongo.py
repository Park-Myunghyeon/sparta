from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# mongodb에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})
# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find())

# # 참고) MongoDB에서 특정 조건의 데이터 모두 보기
# same_ages = list(db.users.find({'age':21}))
#
# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기
#
# for user in all_users:      # 반복문을 돌며 모든 데이터 보기
#     print(user)


# 넣을때 insert_one(), 찾을때find()


user = db.users.find_one({'name':'bobby'})
print (user)

# 그 중 특정 키 값을 빼고 보기
user = db.users.find_one({'name':'bobby'},{'_id':0})

#{'_id':0}, 0은 false의 의미, id값 가져오지마라
print (user)

# 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게 바꿀지 })

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print (user)


db.users.update_many({ }, {'$set':{'age':20}})
# print(all_users)

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print (user)