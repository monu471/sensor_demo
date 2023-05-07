import pandas as pd
import os,sys
from sensor.config import mongo_client

def get_collection_as_dataframe(database:str,collection:str)-> pd.DataFrame:
    df = pd.DataFrame(list(mongo_client[database][collection].find()))
    if "_id" in df.columns:
        df = df.drop("_id",axis=1)
    return df