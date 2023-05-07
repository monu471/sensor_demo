from sensor.utils import get_collection_as_dataframe
import os,sys
import pandas as pd
database = "aps"
collection = "sensor"

if __name__=="__main__":
    try:
        get_collection_as_dataframe(database=database,collection=collection)
    except Exception as e:
        print(e) 



