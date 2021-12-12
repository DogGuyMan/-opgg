import numpy
import pandas as pd
import numpy as np
from pandas.core import series

score_col = ["이름", "국어", "수학"]
score_dic = {"이름": ['A', 'B'], "국어": [60, 80], "수학": [100, 90]}
score_dic2 = {"이름": ['C', 'D'], "국어": [55, 19], "수학": [0, 20]}
df_tuple1 = ["A", 60, 100]
df_tuple2 = ["B", 80, 90]
df_tuple3 = ["E", 100, 70]


def print_emp(df):
    print("=" * 50)
    print(df)
    print("=" * 50)
######################################################################
# SQL로 해당하면 CREATE DROP ALTER의 역활을 보자
# 1. col으로 테이블 cole 만들기
# 2. 딕셔너리로 테이블 만들기
# 3. col과 튜플의 조합으로 테이블 만들기
# --------------------------------------------------------------------


def CREATE_DF_cols():
    df = pd.DataFrame(columns=score_col)
    print(df)


def CREATE_DF_dic():
    df = pd.DataFrame(data=score_dic)
    print(df)


def CREATE_DF_tuple():
    df = pd.DataFrame(np.array([df_tuple1, df_tuple2]), columns=score_col)
    print(df)


def ALTER_ADD_DF_addrow():
    df1 = pd.DataFrame(data=score_dic)
    df1.insert(0, "계", 0)
    df2 = pd.DataFrame(data=score_dic)
    df2.insert(df2.shape[1], "계", 0)
    print_emp(df1)
    print_emp(df2)


def ALTER_ADD_DF_cal():
    df = pd.DataFrame(data=score_dic)
    df["계"] = df["국어"] + df["수학"]
    print_emp(df)


def DROP_DF_col():
    df = pd.DataFrame(data=score_dic)
    df = df.drop(columns=["국어"])
    print_emp(df)

######################################################################
# SQL로 해당하면 DCL 역활을 보자
# 1. 행, 열 각각 시리즈 가져오기
# --------------------------------------------------------------------


def SELECT_DF_col():
    df = pd.DataFrame(data=score_dic)
    print_emp(df["이름"])


def SELECT_DF_row():
    df = pd.DataFrame(data=score_dic)
    print_emp(df[df["이름"] == "A"])


def INSERT_DF_append():
    df = pd.DataFrame(score_dic)
    df2 = pd.DataFrame(data=[df_tuple3], columns=score_dic.keys())
    df = df.append(df2)
    print_emp(df)

######################################################################


def DF_Drop_Isort():
    df = pd.DataFrame(score_dic)
    df2 = pd.DataFrame(score_dic2)
    df = df.append(df2)
    df = df.append(pd.DataFrame(data=[df_tuple3], columns=score_col))
    print("인덱스 정렬이전")
    print_emp(df)
    df = df.reset_index(drop=True)
    print("인덱스 정렬이후")
    print_emp(df)


def main():
    DF_Drop_Isort()


main()
