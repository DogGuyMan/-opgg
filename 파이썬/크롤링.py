import requests
import csv
import os
from requests.api import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import time

print(pd.__version__)
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

raw_DF = pd.read_csv("sample2.csv", sep=",")

platform = {"eun1": "eune", "euw1": "euw", "jp1": "ja",
            "kr": "kr", "la1": "lan", "la2": "las", "ru": "ru"}


def assem_platform_url(_resion):
    assem_p_url = "https://www.leagueofgraphs.com/" + _resion + "/"
    return assem_p_url


def get_user_status(_user):
    driver.find_element(By.CLASS_NAME, "search_field").send_keys(_user)
    # driver.find_element_by_css_selector(".search_field").send_keys(Keys.ENTER)


def find_data():
    for r in platform:
        driver.get(assem_platform_url(r))
        for u in:
            get_user_status(u)


def validate_spell(one_line_class):
    spell_position = one_line_class.find_element_by_css_selector(".spells")
    # if 3번째가 점멸이 아니다.
    return False


def get_data(info):
    if info is None:
        return 'None'
    else:
        return info.get_text().strip()


driver.get(assem_platform_url("kr"))

search_bar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.medium-20.small-18.columns.relative > input.search_field")))

    driver.find_element_by_css_selector(
        "div.medium-20.small-18.columns.relative > input.search_field").send_keys("향긋함")
    driver.find_element_by_css_selector(
        "div.medium-20.small-18.columns.relative > input.search_field").send_keys(Keys.ENTER)

    aapath = WebDriverWait(driver, timeout=5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#mainContent > div.row > div.medium-13.small-24.columns > div:nth-child(5) > table > tbody")))

    sel_ = "#mainContent > div.row > div.medium-13.small-24.columns > div:nth-child(5) > table > tbody >"


valudate_F_falsh_user = True
count = 0
   for i in range(2, 9):
        F_spell = driver.find_element_by_css_selector(
            sel_ + f" tr:nth-child({i}) > td.championCellLight > a > div.spells > div:nth-child(3) > img")
        if F_spell.get_attribute("tooltip-var") == "spell-4":
            count += 1

    if count < 5:
        valudate_F_falsh_user = False

    print(valudate_F_falsh_user)
    불러온 데이터 마지막에 F스펠 데이터 프레임 변수 넣기
###
