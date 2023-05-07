import pandas as pd
import json
import pymongo 
from dataclasses import dataclass
import os,sys

@dataclass
class EnvironmentVarible:
    mongo_db_url = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVarible()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)