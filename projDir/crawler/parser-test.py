# parser.py
import requests

# HTTP GET Request
req = requests.get('http://www.gukbi.com/')
# print(req)

# HTML 소스 가져오기
html = req.text
print(html)

# HTTP Header 가져오기
header = req.headers
# print(header)

# HTTP Status 가져오기 (200: 정상)
status = req.status_code
# print(status)

# HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok
# print(is_ok)