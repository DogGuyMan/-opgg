import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

platform = {"eun1": "eune", "euw1": "euw", "jp1": "jp",
            "kr": "kr", "la1": "lan", "la2": "las", "ru": "ru"}
platform_key = platform.keys()


def assem_url(_region, _user):
    assem_p_url = f"https://{_region}.op.gg/summoner/userName={_user}"
    return assem_p_url


raw_DF = pd.read_csv("ALL_DF_CP949.csv", sep=",", encoding="cp949")


def ex():
    print("start " + "7698")
    req = requests.get(assem_url("kr", "7698"),  headers={
        "User-Agent": "Mozilla/5.0"})
    html = req.text
    opsoup = bs(html, 'html.parser')
    getPoint = opsoup.select_one(
        "div.TierRankInfo > div.TierInfo > span.LeaguePoints")
    if getPoint == None:
        print("랭크가 없음")
    else:
        print(int(getPoint.text.strip()[0: -3].replace(",", "")))


restartList = list()


ex()

######################################

for plat in platform_key:
    DF_PointList = pd.DataFrame(index=range(0, 3), columns=[
                                "region", "summonerName, rankPoint"])

    for i in range(0, raw_DF.shape[0]):
        curRaw = raw_DF.iloc[i]
        print("start " + platform[curRaw["region"]],
              curRaw["summonerName"])

        req = requests.get(assem_url(platform[curRaw["region"]], curRaw["summonerName"]),  headers={
            "User-Agent": "Mozilla/5.0"})
        if req.status_code == 200:
            html = req.text
            opsoup = bs(html, 'html.parser')

            getPoint = opsoup.select_one(
                "div.TierRankInfo > div.TierInfo > span.LeaguePoints")

            if getPoint == None:
                print("랭크가 없음")
                curPoint = -5000
            else:
                curPoint = int(getPoint.text.strip()[0: -3].replace(",", ""))

            DF_PointList = DF_PointList.append(
                [curRaw["region"], curRaw["summonerName"], curPoint], ignore_index=True)

        else:
            restartList.append(curRaw["summonerName"])
            time.sleep(200)


print(restartList)
DF_PointList.to_csv(f'ALL_rankPoint.csv',
                    index=False, header=True, na_rep='-')
"""
    raw_DF.to_csv(f'ALL_{platform[plat]}_DorF.csv',
                  index=False, header=True, na_rep='-')
    """
