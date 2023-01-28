import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"D:\Project series\proj_1\proj_3_insurance-pemium-prediction\insurance.csv")
DATABASE_NAME = "INSURANCE_PREMIUM_PREDICTION"
COLLECTION_NAME = "INSURANCE_EXPENSES_RAW DATA"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

'''
class MongoDB(object):

    def __init__(self,dbName=None, collectionName=None):
        self.dbName=dbName
        self.collectioName= collectionName
        self.client = pymongo.MongoClient("mongodb+srv://abhi0557:abhi29894@clustor0.zr9ru.mongodb.net/?retryWrites=true&w=majority")
        self.DB = self.client[self.dbName]
        self.collection = self.DB[self.collectioName]


    def InsertData(self,path=None):
        df= pd.read_csv(path)
        data= df.to_dict('records')

        self.collection.insert_many(data)
        print("All the data has been exported to mongoDb server....")

if __name__=="__main__":
    mongodb= MongoDB(dbName="INSURANCE_PREMIUM_PREDICTION", collectionName="INSURANCE_EXPENSES_RAW DATA")
    mongodb.InsertData(path= "D://Project series//proj_1//proj_3_insurance-pemium-prediction//insurance.csv")
'''



    