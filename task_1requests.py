import requests


URL = 'http://pulse-rest-testing.herokuapp.com/books'
PARAMS = {'Content-type': 'application/json'}
DATA = {'title': 'TesterPro','author': 'Timur H'}
#1
post_req = requests.post(url = URL, data= DATA)
print(post_req.status_code, post_req.reason ,post_req.json())
#2
created_item = post_req.json()
get_req = requests.get(url=URL+'/{}'.format(created_item['id']), params=PARAMS)
print(get_req.status_code, get_req.reason ,get_req.json())
#3
get_req = requests.get(url=URL, params=PARAMS)
for i in get_req.json():
    if i['id'] == created_item['id']:
        print(get_req.status_code, get_req.reason, i)
#4
put_data = {'title': 'TesterProChanged'}
put_req = requests.put(url=URL+'/{}'.format(created_item['id']), data=put_data)
print(put_req.status_code, put_req.reason ,put_req.json())
#5
changed_item = put_req.json()['id']
get_req = requests.get(url=URL+'/{}'.format(changed_item), params=PARAMS)
print(get_req.status_code, get_req.reason ,get_req.json())
#6
get_req = requests.get(url=URL, params=PARAMS)
for i in get_req.json():
    if i['id'] == changed_item:
        print(get_req.status_code, get_req.reason, i)
#7
del_req = requests.delete(url=URL+'/{}'.format(changed_item))
print(del_req.status_code, del_req.reason)
