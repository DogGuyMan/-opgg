import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

col = [
    "region",
    "rank",
    "division",
    "summonerName",
    "win",
    "lose",
    "winRatio"
]
DF_colums = pd.DataFrame(columns=col)
platform = {"eun1": "eune", "euw1": "euw", "jp1": "jp",
            "kr": "kr", "la1": "lan", "la2": "las", "ru": "ru"}


def assem_url(_region, _user):
    assem_p_url = f"https://{_region}.op.gg/summoner/userName={_user}"
    return assem_p_url


def validate_region(region):
    if region == "eun1":
        return 0
    elif region == "euw1":
        return 1
    elif region == "jp1":
        return 2
    elif region == "kr":
        return 3
    elif region == "la1":
        return 4
    elif region == "la2":
        return 5
    else:
        return 6


def division_add(_div):
    NumNPoint = list()
    if _div == "I":
        NumNPoint = [0, 300]
    elif _div == "II":
        NumNPoint = [1, 200]
    elif _div == "III":
        NumNPoint = [2, 100]
    elif _div == "IV":
        NumNPoint = [3, 0]

    return NumNPoint


def validate_ALL(_curRow):
    playNum = _curRow["win"] + _curRow["lose"]
    regionINT = validate_region(_curRow["region"])
    if (_curRow["division"] == "-"):
        if(_curRow["rank"] == "CHALLENGER"):
            rankINT = 0
        elif(_curRow["rank"] == "GRANDMASTER"):
            rankINT = 1
        elif(_curRow["rank"] == "MASTER"):
            rankINT = 2
        rankPoint = 2000
    else:
        NumNPoint = division_add(_curRow["division"])
        if(_curRow["rank"] == "DIAMOND"):
            rankINT = 3 + NumNPoint[0]
            rankPoint = 1600 + NumNPoint[1]
        elif(_curRow["rank"] == "PLATINUM"):
            rankINT = 7 + NumNPoint[0]
            rankPoint = 1200 + NumNPoint[1]
        elif(_curRow["rank"] == "GOLD"):
            rankINT = 11 + NumNPoint[0]
            rankPoint = 800 + NumNPoint[1]
        elif(_curRow["rank"] == "SILVER"):
            rankINT = 15 + NumNPoint[0]
            rankPoint = 400 + NumNPoint[1]
        elif(_curRow["rank"] == "BRONZE"):
            rankINT = 19 + NumNPoint[0]
            rankPoint = 0 + NumNPoint[1]
    resList = [playNum, regionINT, rankINT, rankPoint]
    print(_curRow["summonerName"], resList)
    return resList


def getPoint(_curRow, _list):
    req = requests.get(
        assem_url(
            platform[_curRow["region"]],
            _curRow["summonerName"]),
        headers={"User-Agent": "Mozilla/5.0"}
    )
    print("start " + platform[_curRow["region"]],
          _curRow["summonerName"])
    if req.status_code == 200:
        html = req.text
        opsoup = bs(html, 'html.parser')
        getHisbox = opsoup.find("div", {'class': 'GameItemList'})

        if(getHisbox != None):
            getPoint = opsoup.select_one(
                "div.TierRankInfo > div.TierInfo > span.LeaguePoints")
            if getPoint == None:
                print("랭크가 없음")
                curPoint = -5000
            else:
                curPoint = int(getPoint.text.strip()[0: -3].replace(",", ""))
                print(curPoint)

            _list[3] += curPoint
        else:
            _list[3] = -5000
    else:
        return [_list[0], _list[1], _list[2], -12345678]
    return _list


"""
platform_val = platform.values()
for plat in platform_val:
    raw_DF = pd.read_csv(f"Sub_{plat}_DorF.csv", sep=",")
    raw_DF = raw_DF[raw_DF["DorF"] != 0]
    DF_colums = pd.concat([DF_colums, raw_DF], axis=0, ignore_index=True)

DF_colums.to_csv(f'Sub_AllDorF.csv', index=False, header=True, na_rep='-')
"""
"""
CHALL_DF = pd.read_csv("Chall_AllDorF.csv", sep=",")
SUB_DF = pd.read_csv("Sub_AllDorF.csv", sep=",")
ALL_DF = pd.concat([CHALL_DF, SUB_DF], axis=0, ignore_index=True)

ALL_DF.to_csv(f'ALL_DF.csv', index=False, header=True, na_rep='-')
"""
ALL_DF = pd.read_csv("ALL_DF.csv", sep=",", encoding="UTF-8")

#ALL_DF["winRatio_By_100"] = ALL_DF["winRatio"] * 100
#ALL_DF.to_csv(f'ALL_DF.csv', index=False, header=True, na_rep='-')

DF_playNum_rankINT_rankPoint_regionINT = pd.DataFrame(index=range(
    0, 4), columns=["playNum", "rankINT", "rankPoint", "regionINT"])

for i in range(0, ALL_DF.shape[0]):
    curRow = ALL_DF.iloc[i]
    LIST_TEMP_NUM_INTS = getPoint(curRow, validate_ALL(curRow))
    DF_playNum_rankINT_rankPoint_regionINT = DF_playNum_rankINT_rankPoint_regionINT.append(
        LIST_TEMP_NUM_INTS, ignore_index=True)

pd.DataFrame(DF_playNum_rankINT_rankPoint_regionINT).to_csv(
    f'DF_expend_data.csv', index=False, header=True, na_rep='-')
