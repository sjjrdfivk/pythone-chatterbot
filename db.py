import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 新建数据库
mydb = myclient["chatterbot"]

dblist = myclient.list_database_names()
if "chatterbot" in dblist:
    print("数据库已存在！")
else:
    print("数据库不存在！")

# 创建集合
mycoll = mydb["bot"]

# 判断集合是否存在
collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "bot" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")

# 插入单个文档
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycoll.insert_one(mydict)

# 插入多个文档
# mylist = [
#   {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#   {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#   {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#   {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#   {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
# x = mycoll.insert_many(mylist)

# for x in mycoll.find():
#     print(x)

# 修改
# mycoll.update_many({"alexa": "10000"}, {"$set": {"alexa": "11"}})

# 排序 1 为升序，-1 为降序，默认为升序。
# mydoc = mycoll.find().sort("alexa", -1)
# for x in mydoc:
#     print(x)

# 删除数据
# myquery = {"name": {"$regex": "^F"}}
# x = mycoll.delete_many(myquery)
# print(x.deleted_count, "个文档已删除")
