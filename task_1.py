import http.client
import json
#1
conect = http.client.HTTPConnection('pulse-rest-testing.herokuapp.com')
body = json.dumps({'name': 'Timur','type': 'Tester', 'level': 10, 'book': 145})
headers = {'Content-type': 'application/json'}
conect.request('POST', '/roles', body=body, headers=headers)
response = conect.getresponse()
created_id = json.loads(response.read())['id']
print(response.status, response.reason, 'id = {}'.format(created_id))
#2
conect.request('GET', '/roles/{}'.format(created_id))
response = conect.getresponse()
if created_id in json.loads(response.read()).values():
    print(response.status, response.reason, 'ITEM IS PRESENT')
#3
conect.request('GET', '/roles/')
response = conect.getresponse()
items_list = json.loads(response.read())
for i in items_list:
    if i['name'] == 'Timur':
        print(i['id'], end=' ')

#4
conect.request('PUT', '/roles/{}'.format(items_list[0]['id']), body = json.dumps({'name': 'Changed'}), headers= headers)
response = conect.getresponse()
print('\n', response.status, response.reason)
#5
conect.request('GET', '/roles/{}'.format(items_list[0]['id']))
response = conect.getresponse()
if json.loads(response.read())['name'] == 'Changed':
    print(response.status, response.reason, 'ITEM name WAS CHANGED')
#6
conect.request('GET', '/roles/')
response = conect.getresponse()
items_list = json.loads(response.read())
for i in items_list:
    if i['name'] == 'Changed':
        print(i['id'], end=' ')
#7
for i in items_list:
    if i['name'] == 'Changed' or i['name'] == 'Timur':
        conect.request('DELETE', '/roles/{}'.format(i['id']))
        response = conect.getresponse()
        print(response.status, response.reason, 'ITEM name WAS DELETED')