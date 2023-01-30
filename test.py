import requests

open('test.txt','w').write(requests.get(url="https://raw.githubusercontent.com/snowflake677/test/main/test.txt").content.decode())