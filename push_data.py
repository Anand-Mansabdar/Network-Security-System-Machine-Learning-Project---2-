import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecuritySystemException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")
# print(MONGO_DB_URL)  # To check if your environment variables are being loaded

ca = certifi.where()

class NetworkDataExtract():
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise NetworkSecuritySystemException(e, sys)
    
  # To read the dataset and convert it to json
  def csv_to_json(self, file_path):
    try:
      data = pd.read_csv(file_path)
      data.reset_index(drop=True, inplace=True)
      records = list(json.loads(data.T.to_json()).values())
      return records
    except Exception as e:
      raise NetworkSecuritySystemException(e, sys)
    
  # A function to insert data in MongoDB Atlas
  def insert_data_in_mongodb(self, records, database, collection):
    try:
      self.records = records
      self.database = database
      self.collection = collection
      
      self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
      self.database = self.mongo_client[self.database]
      self.collection = self.database[self.collection]
      
      self.collection.insert_many(self.records)
      return len(self.records)
    except Exception as e:
      raise NetworkSecuritySystemException(e, sys)
    
if __name__ == "__main__":
  FILE_PATH = "Network_Data\phishingData.csv"
  DATABASE = "NetworkSecuritySystem"
  COLLECTION = "NetworkData"
  network_obj = NetworkDataExtract()
  records = network_obj.csv_to_json(FILE_PATH)
  print(records)
  number_of_records = network_obj.insert_data_in_mongodb(records=records, database=DATABASE, collection=COLLECTION)
  
  print(number_of_records)