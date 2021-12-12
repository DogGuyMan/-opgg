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


restartList = list()
######################################
for plat in platform_key:
    raw_DF = pd.read_csv(f"Sub_{plat}.csv", sep=",")

    DF_LIST = list()
    for i in range(0, raw_DF.shape[0]):
        print("start " + platform[raw_DF.iloc[i]["region"]],
              raw_DF.iloc[i]["summonerName"])

        req = requests.get(assem_url(platform[raw_DF.iloc[i]["region"]], raw_DF.iloc[i]["summonerName"]),  headers={
            "User-Agent": "Mozilla/5.0"})
        if req.status_code == 200:
            html = req.text

            getHisbox = bs(html, 'html.parser').find(
                "div", {'class': 'GameItemList'})

            if(getHisbox != None):
                getHis = getHisbox.find_all("div", {'class': 'GameItemWrap'})
                curDorF = 0
                countD = 0
                countF = 0
                for i in range(1, len(getHis)):
                    getspell = getHis[i].find_all("div", {'class': 'Spell'})
                    if ((getspell[0].find()['alt'] == "Flash") | (getspell[1].find()['alt'] == "Flash")):
                        if (getspell[1].find()['alt'] == "Flash"):
                            countF = countF + 1
                        if (getspell[0].find()['alt'] == "Flash"):
                            countD = countD + 1
                            # Reverse1라는 카타 아칼리 장인은 뭘까..
                if((countD == 0) & (countF == 0)):
                    curDorF = 3
                elif ((countD < countF) & (countF > ((len(getHis) * 3) / 4))):
                    curDorF = 1
                else:
                    curDorF = 2
            else:
                curDorF = 0

            DF_LIST.append(curDorF)
            print(curDorF)
        else:
            restartList.append(raw_DF.iloc[i]["summonerName"])
            time.sleep(200)

    DF_COL = ["DorF"]
    DF_dataFrame = pd.DataFrame(data=DF_LIST, columns=DF_COL)
    print(DF_dataFrame)
    print(restartList)
    raw_DF = pd.concat([raw_DF, DF_dataFrame], axis=1)
    raw_DF.to_csv(f'Sub_{platform[plat]}_DorF.csv',
                  index=False, header=True, na_rep='-')

"""
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.implicitly_wait(15)  # 묵시적 대기, 활성화를 최대 15초가지 기다린다.
"""

"""
def validate_working():
    WebDriverWait(driver, timeout=5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.Information > span.Name")
                                       )
    )
    getName = driver.find_element_by_css_selector(
        "div.Information > span.Name")

    print(getName.get_attribute("class"))
"""

"""
def spell_find_algo():
    print("spell_find_algo")
    WebDriverWait(driver, timeout=2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.GameItemList")
                                       )
    )
    getGameList = driver.find_element_by_css_selector(
        "div.GameItemList")

    countD = 0
    countF = 0
    for i in range(1, 8):
        getSpellD = getGameList.find_element_by_css_selector(
            f"div:nth-child({i}) > div > div.Content > div.GameSettingInfo > div.SummonerSpell > div:nth-child({1}) > img")
        getSpellF = getGameList.find_element_by_css_selector(
            f"div:nth-child({i}) > div > div.Content > div.GameSettingInfo > div.SummonerSpell > div:nth-child({2}) > img")
    if(countD == 0 & countF == 0):
        print("점멸을 아예 사용안함")
        curDorF = 3
    elif ((countD < countF) & (countF > 8)):
        curDorF = 1
    else:
        curDorF = 2

def IS_Found_Page():
    try:
        driver.find_element_by_css_selector("div.SummonerNotFoundLayout")
    except Exception as error:
        return True
    return False

"""
"""
for i in range(0, raw_DF.shape[0]):
    print("=" * 50)
    driver.get(
        assem_url(platform[raw_DF.iloc[i]["region"]], raw_DF.iloc[i]["summonerName"]))

    if(IS_Found_Page()):
        DF_LIST.append(spell_find_algo())
    else:
        DF_LIST.append(0)

DF_dataFrame = pd.DataFrame(data=DF_LIST, columns="DorF")

raw_DF = pd.concat([raw_DF, DF_dataFrame], axis=1)
time.sleep(5)
driver.quit()  # 웹 브라우저 종료. driver.close()는 탭 종료
"""
