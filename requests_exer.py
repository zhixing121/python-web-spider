import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth


params = {'username': 'ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# print(r.text)
print("Cookie is set to:")
print(r.cookies.get_dict())
print('------------')
print('going to profile page...')
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)


session = requests.Session()
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# print(r.text)
print("Cookie is set to:")
print(s.cookies.get_dict())
print(s.headers)
print('------------')
print('going to profile page...')
r = session.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)


auth = HTTPBasicAuth('ryan', 'password')
Hr = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(Hr.text)