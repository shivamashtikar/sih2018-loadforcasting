from pymongo import MongoClient
from bson import Binary
import datetime.datetime
client = MongoClient(host='192.168.0.230')
db = client.zones


class FetchData:
    @staticmethod
    def getTrainData(self,zone):
        val = {'temp':[],'date':[],'hour':[],'month':[],'weekday':[],'load':[]}
        curs=db['zone'+str(zone)].find()
        for doc in curs:
            val['temp'].append(doc['temp'])
            val['hour'].append(doc['hour'])
            val['weekday'].append(doc['weekday'])
            val['load'].append(doc['load'])
            val['date'].append(doc['date'])
            val['month'].append(doc['month'])
        return val
    @staticmethod
    def storeObj(self,pickleobj,zone,acc,name='{0}{1}{2}{3}'.format(da.day,da.month,da.year,da.hour)):
        da = datetime.datetime.now()
        db = client.picklestore
        col = db['zone'+str(zone)]
        dic = {'_id':name,'obj':Binary(pickleobj),'accuracy':acc}
        col.insert(dic)
    @staticmethod
    def setCurrentObj(self,obj,zone,name):
        db = client.picklestore
        col = db['currentWrkObj']
        col.update({'_id':zone},{'$set':{'_id':zone,'obj':Binary(obj),'name':name}},{'$upsert':True})

    @staticmethod
    def get_current_obj(zone):
        db = client.picklestore
        col = db['currentWrkObj']
        val = col.find({'zone':zone})
        return val
    @staticmethod
    def get_obj(name,zone):
        oid = str(name)
        db = client.picklestore
        col = db['zone' + str(zone)]
        dic = col.find({'_id':oid})
        return dic['obj']

if __name__ == '__main__':
    s = FetchDataUnit()