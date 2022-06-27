# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request # 특정 U
import json



client_id = "w14leLn7edmBDpjMriJo"
client_secret = "xILNWxTK73"

encText = urllib.parse.quote("어벤져스")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과를 query에 매칭되는 데이터를 붙여줬다  
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText

# API를 요청하는 사람이 누군지에 대한 정보도 넘겨주어야 하기 때문에 아래의 add_header에 client _id, client_secret 이 필요
request = urllib.request.Request(url) # request 객체가 필요할 때 요청한다.
request.add_header("X-Naver-Client-Id",client_id) # 머리말 부분에 내가 누군지에 대한 정보를 포함시킨다.
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request) # request를 보냈을 때, 반환받는 객체를 response 객체 라고 한다.

rescode = response.getcode() # getcode를 통해 잘 받아졌는지 확인할 수 있다.
if(rescode==200):
    response_body = response.read() # response 객체에 있는 것을 읽어들이겠다
    # print(response_body.decode('utf-8')) # utf-8 로 디코딩해서 읽어야겠다.
else:
    print("Error Code:" + rescode)

resdata = response_body.decode('utf-8')
# with open('movie.json', 'w',encoding='UTF-8-sig') as file:
#     file.write(json.dumps(resdata, ensure_ascii=False)) # 갖고온 json 파일을 쓸거다 그리고 한국어를 제대로 보기위한 설정을 한다

pydata = json.loads(resdata)
data = pydata['items']

print(data[0]['title'])

