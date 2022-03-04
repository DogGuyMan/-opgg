# crawling-opgg-with-BS4
riotapi를 통해 랜덤추출한 유저이름을 넣어서 유저의 정보를 가져오는 프로젝트

# 개요
riot api를 통해 임의로 표본 추출한 유저의 **소환사 이름** 가 저장된 CSV 파일을 사용해

opgg에게 request 

F 점멸 ,D 점멸, 혹은 어느것도 사용하지 않는 유저를 
판별하고, F,D 유저 비율을 확인하고 CSV롤 저장

### 1. 사용 라이브러리
pandas : 데이터 프레임을 다루기 위함
requests : URL 을 리퀘스트 
BeautifulSoup : 크롤링에 사용할 라이브러리

### 2. 변수, 자료

### 전역
1. platform 
   * 서버 플랫폼
     * key : 라이엇 api가 설정한 국가 이름
     * value : opgg에서 이용해야할 국가 이름 
    ```py
    platform = {"eun1": "eune", "euw1": "euw", "jp1": "jp","kr": "kr", "la1": "lan", "la2": "las", "ru": "ru"}
    ```

#### 반복문 내부
1. raw_DF
   * 입력으로 들어온 CSV파일 데이터프레임
   * raw_DF.iloc[i]
      * 데이터 프레임 에서 행을 인덱스로 접근할 때 사용됨
<br> 

2. DF_LIST
   * 여기서 DF는 D 점멸 F 점멸의 약자임..
      * 데이터 프레임을 의미하는게 아니다..(컨벤션 다시 하기)
   * 리스트에 들어가는 범주값

```txt
1 : F 점멸사용자
2 : D 점멸 사용자
3 : 어느것도 사용 안하는사람
  ex) 1. 유체화 누누 유저
      2. 점화텔 카타리나 유저
      3. 점화텔 아칼리 유저
0 : 플레이어를 검색할 수 없을때
  ex) 1. 전적이 없음
      2. 닉변해서 찾을수 없는유저
      3. 삭제되어 찾을수 없는 유저
```
<br>

3. req, html, getHisbox

* I. req 
   * request.get("url") 
* II. html
  * req 한것을 text로 가져오기
* III. getHisbox
  * 전적이 표시되는 html div

### 개선해야할 점
함수 리펙토링, 전역변수 지역변수의 활용을하여
좀더 가독성을 높여야 생각,
