import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

response = requests.get(url)

html="""
<nav class="menu-box-1" id="menu-box">
    <ul>
        <li>
            <a href="https://www.naver.com">네이버로 이동</a>
        </li>
        <li>
            <a href="https://www.naver.com">네이버로 이동</a>
        </li>
        <li>
            <a href="https://www.google.com">구글로 이동</a>
        </li>
        <li>
            <a href="https://www.daum.com">다음으로 이동</a>
        </li>
        <li>
    </ul>
</nav>
"""
soup = BeautifulSoup(html, "html.parser")

a_tags = soup.select("a")
# a_tag = soup.select_one("a")

# print(a_tags)

for tags in a_tags:
    print(tags.get("href"))