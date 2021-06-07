import requests
from bs4 import BeautifulSoup


# Webページを取得して解析する
# 58066
url = "https://unistyleinc.com/entry_sheets/43293"
response = requests.get(url)
response.encoding = response.apparent_encoding
bs = BeautifulSoup(response.text, 'html.parser')

print(bs.title.text)
print(bs.h3.text)
print(bs.find_all("div", class_="esdetail_main")[0])




response.close()


# # HTML全体を表示する
# print(soup)
#  <title>
# <h3 class="fg esdetail_subtitle">
# <div class="esdetail_main" id="dldetail_body">
