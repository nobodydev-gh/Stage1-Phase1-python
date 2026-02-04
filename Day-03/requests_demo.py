import requests


r=requests.get('https://www.wikipedia.org/')

print(dir(r))

print(r.text)


print(r.status_code)


print(r.headers)