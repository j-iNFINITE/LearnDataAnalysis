# -*- coding: utf-8 -*-
from dataapi import Client
from pandas import Series, DataFrame
import pandas as pd
import json
import datetime
client = Client()
client.init('')
def get_foundlist():  #基金列表
    url = '/api/master/getSecID.json?field=&assetClass=F&ticker=&partyID=&cnSpell='
    code,result = client.getData(url)
    if code==200:
        jsonfile = json.loads(result.decode('gbk'))
        data = jsonfile['data']
        frame = DataFrame(data)
        return frame['ticker'].values

    else:
        print(code)
        print(result)
def getFundNav(datelist):
    for date in datelist:
        url = '/api/fund/getFundNav.json?field=&beginDate=&endDate=&secID=&ticker=&dataDate=%s' %(date)
        code,result = client.getData(url)
        if code==200:
            print(result)
            jsonfile = json.loads(result.decode('gbk'))
            data = jsonfile['data']
            frame = DataFrame(data)
            print(frame)
        else:
            print(code)
            print(result)
def datelist(start,end):
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

if __name__ == "__main__":
    # tickers = get_foundlist()
    getFundNav(['20141008','20150531'])