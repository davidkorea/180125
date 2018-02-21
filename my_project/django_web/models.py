from mongoengine import *
from mongoengine import connect
connect('awms', host='127.0.0.1', port=27017)

class LogInfo(Document):
    caseid = StringField()
    problem = StringField()
    custtpye = StringField()
    orgnization = StringField()
    handle_by = StringField()
    city = StringField()
    no = StringField()
    date = StringField()
    attachment = StringField()
    solution = StringField()
    source = StringField()
    resolved = StringField()
    note = StringField()

    meta ={'collection':'loginfo_backup'}

# for i in LogInfo.objects[:10]:
#     print(i.caseid, i.date)

# pipeline = [
#     {'$match': {'$and': [{'date':{'$gte':'2017/01/01','$lte':'2018/01/09'}},{'handle_by':'Andy Tsao'}]}},
#     {'$group': {'_id':'$city', 'counts': {'$sum': 1}}},
#     {'$sort':{'counts':-1}},
#     {'$limit':10}
# ]
# for i in LogInfo._get_collection().aggregate(pipeline):
#     print(i)