import requests
import json
import re
import numpy as np
import pprint

url='https://apiv2.twitcasting.tv/internships/2019/games?level=2'
token={token}
operator=np.array(['+','-', '*', '/'])


def calculate(arr,sum,opr,i):#数字セットと演算子セットを引数にする
  if   opr[i] == '+':
    sum=  sum+arr[i+1];
  elif opr[i] == '-':
    sum = sum-arr[i+1]
  elif opr[i] == '*':
    sum = sum*arr[i+1]
  elif opr[i] == '/':
    sum = sum/arr[i+1]
  if i<len(arr)-2:
    i=i+1
    sum=calculate(arr,sum,opr,i)#再帰
  return sum



headers  = {"content-type": "application/json",'Authorization': token}
r=requests.get(url,headers=headers)
data=r.json()
id=data['id']
question=data['question']
d = re.search("(.*)=(.*)", question)
num=np.array(d.group(1).rsplit("?"),np.int32)
ans=int(d.group(2))
print(data)
print(num)
print(ans)

for a in range(0,4):#演算パターンを逐次遂行
  for b in range(0,4):
    for c in range(0,4):
      for d in range(0,4):
        answer= calculate(num,num[0],np.array([operator[a],operator[b],operator[c],operator[d]]),0)
        if answer==ans:
          break
      if answer==ans:
        break
    if answer==ans:
      break
  if answer==ans:
    break
my_ans=operator[a]+operator[b]+operator[c]+operator[d]
print(my_ans)
response = requests.post('https://apiv2.twitcasting.tv/internships/2019/games/'+id,json.dumps({"answer":my_ans}),headers={"content-type": "application/json",'Authorization': token})
print(response.json())