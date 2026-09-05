
import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ca=certifi.where()# Get the path to the file containing trusted CA certificates.
#It returns the path to the .pem file (a file that contains trusted certificates).


import pandas as pd
import numpy as np
import pymongo

from src.exception.exception import Networksecurityexception
from src.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise Networksecurityexception(e,sys)
        

    def csv_to_json_convertor(self,file_path):
            
            try:
                data=pd.read_csv(file_path)
                # data.reset_index(drop=True,inplace=True)
                records=list(json.loads(data.T.to_json()).values())
                return records
            except Exception as e:
                raise Networksecurityexception(e,sys)
            
    def insert_data_mongodb(self,records,database,collection):
            try:
                self.database=database
                self.collection=collection
                self.records=records

                self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
                self.database=self.mongo_client[self.database]
                self.collection=self.database[self.collection]
                self.collection.insert_many(self.records)
                return (len(self.records))
            except Exception as e:
                raise Networksecurityexception(e,sys)


if __name__=="__main__":
    FILE_PATH="data\cleaned data\clean_data.csv"
    DATABASE="data__011"
    collection="demand_Data"
    networkobj= NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    ho_of_records=networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(ho_of_records)