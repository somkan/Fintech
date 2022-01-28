import streamlit as st
import pymongo
import pandas as pd
from fyers_api import fyersModel, accessToken
from datetime import date
import os

myclient = pymongo.MongoClient(
            "mongodb+srv://admin:admin@cluster0.xsz8r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["StockboardDB"]
mycol = mydb["Auth_Data"]
mycol1= mydb["request_token"]
mycol2 = mydb["access_token"]
myJournal = mydb["tjournal"]
myStrategy1= mydb["strategy1"]
myStrategy12=mydb["strategy12"]
userid = "XS06414"

def get_data():
    db = myclient.mydb
    items = db.mycol2.find()
    items = list(items)  # make hashable for st.cache
    return items

items=get_data()

for item in items:
    st.write(item['userid'])
