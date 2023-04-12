import pymongo


# # 创建客户端-方式1
# client = pymongo.MongoClient(host='localhost', port=27017, tz_aware=True)
# print(client)

# 创建客户端-方式2
uri = "localhost:27017"
# uri = "mongodb://%s:%s@%s:%s" % ('root', '123456', '192.168.162.130', 27017)
client = pymongo.MongoClient(uri)
# print(client)

# 创建数据库-方式1
db = client.hair
# print(db)

# # 创建数据库-方式2
# from pymongo.database import Database
# db2 = Database(client=client, name='hair')
# print(db2)
#
# # 创建数据库-方式3
# db3 = client.get_database('hair')
# print(db3)

# 删除数据库
# client.drop_database('ab')

# # 展示所有数据库--show dbs
# for name in client.list_database_names():
#     print(name)


def test_collection():
    # 集合
    # 1.db.books
    books = db.books
    # print(books)

    # # 2.Collection
    # from pymongo.collection import Collection
    # books2 = Collection(db, name='books')
    # print(books2)

    # # 3.get_collection
    # books3 = db.get_collection('books')
    # print(books3)

    # # 4.create_collection 创建集合，没有该集合时，创建
    # book4 = db.create_collection('books')
    # print(book4)

    # # 删除集合
    # db.drop_collection('abc')

    # # show collections
    # for book in db.list_collections():
    #     print(book)


# # 索引的创建，不能超过64个
# def test_index():
#     users = client.hair.users
#     idx = users.create_index([('name', pymongo.ASCENDING)])
#     print(idx)
#     #     降序的索引
#     idx2 = users.create_index([('name',pymongo.DESCENDING)])
#     print(idx2)

def test_insert():
    users = client.hair.users
    r = users.insert_one({'name': 'zs', 'age': 200, 'sex': '女'})
    # print(r)
#     操作状态，被插入后的_id的值
    print(r.acknowledged, r.inserted_id)


if __name__ == '__main__':
    # test_index()
    # test_collection()
    test_insert()