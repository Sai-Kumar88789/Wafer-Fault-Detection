from pymongo import MongoClient
from dotenv import load_dotenv
from wafer.constant.database import DATABASE_NAME,TABLE_NAME
import os,sys
import certifi
from wafer.exception import WaferException
load_dotenv()
ca = certifi.where()
class MongodbClient:
    clinet = None
    def __init__(self,databasename:DATABASE_NAME) -> None:
      
        try:
            if MongodbClient.client is None:
                host = os.getenv("MONGODB_URL")
                MongodbClient.client =  MongoClient(host,tlsCAFile =ca)
            self.client = MongodbClient.client
            self.mydatabase = self.client[databasename]
            self.mytable = self.mydatabase[TABLE_NAME]
            self.databasename = databasename
        except Exception as e:
            raise WaferException(e,sys)
