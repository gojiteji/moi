import requests
import json
import re
import numpy as np
import pprint
url='https://apiv2.twitcasting.tv/internships/2019/games?level=1'
token= {token is here}
def check_all_pattern(arr,cor):
  #愚直に4*4上通り
  if arr[0]+arr[1]+arr[2]==cor:
    return '++'
  if arr[0]+arr[1]-arr[2]==cor:
    return '+-'
  if (arr[0]+arr[1])/arr[2]==cor:
    return '+/'
  if (arr[0]+arr[1])*arr[2]==cor:
    return '+*'

  if arr[0]-arr[1]+arr[2]==cor:
    return '-+'
  if arr[0]-arr[1]-arr[2]==cor:
    return '--'
  if (arr[0]-arr[1])/arr[2]==cor:
    return '-/'
  if (arr[0]-arr[1])*arr[2]==cor:
    return '-*'

  if arr[0]/arr[1]+arr[2]==cor:
    return '/+'
  if arr[0]/arr[1]-arr[2]==cor:
    return '/-'
  if (arr[0]/arr[1])/arr[2]==cor:
    return '//'
  if (arr[0]/arr[1])*arr[2]==cor:
    return '/*'

  if arr[0]*arr[1]+arr[2]==cor:
    return '*+'
  if arr[0]*arr[1]-arr[2]==cor:
    return '*-'
  if arr[0]*arr[1]/arr[2]==cor:
    return '*/'
  if arr[0]*arr[1]*arr[2]==cor:
    return '**'
headers  = {"content-type": "application/json",'Authorization': token}
r=requests.get(url,headers=headers)
print(r)
data=r.json()
print(json.dumps(data, indent=4))
id=data['id']
question=data['question']
d = re.search("(.*)=(.*)", question)
num=np.array(d.group(1).rsplit("?"),np.int32)
ans=int(d.group(2))
print(num)
print(ans)

my_ans=check_all_pattern(num,ans)
print(my_ans)

response = requests.post('https://apiv2.twitcasting.tv/internships/2019/games/'+id,json.dumps({"answer":my_ans}),headers={"content-type": "application/json",'Authorization': token})
pprint.pprint(response.json())





