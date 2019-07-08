import requests
import json
import re
import numpy as np
import pprint
import itertools

url='https://apiv2.twitcasting.tv/internships/2019/games?level=3'
token={token}
operator=np.array(['+','-', '*', '/'])
headers  = {"content-type": "application/json",'Authorization': token}

def calculate(arr,sum,opr,i):#数字セットと演算子セットを引数にする
  if   opr[i] == '+':
    sum=  sum+arr[i+1]
  elif opr[i] == '-':
    sum = sum-arr[i+1]
  elif opr[i] == '*':
    sum = sum*arr[i+1]
  elif opr[i] == '/':
    sum = sum/arr[i+1]
  if isinstance(sum, bool):#答えに小数は発生しない（多分）
    return false
  elif i<len(arr)-2:
    i=i+1
    sum=calculate(arr,sum,opr,i)#再帰
  return sum

def all_operators(arr):#全演算子を回す
  operators=np.array([])

  for operators in itertools.product(operator, repeat=len(num)-1):    
    result=calculate(num,num[0],operators,0)
    if isinstance(result, bool):
      pass#nothing to do
    elif result==ans:
        break
  print("returning"+str(operators))
  return operators



r=requests.get(url,headers=headers)
print(r)
data=r.json()
id=data['id']
question=data['question']
d = re.search("(.*)=(.*)", question)
num=np.array(d.group(1).rsplit("?"),np.int32)
ans=int(d.group(2))
print(data)
print("Q is "+str(num))
print("A is "+str(ans))

my_ans=all_operators(num)
my_ans="".join(my_ans)
print("My answer is "+str(my_ans))

response = requests.post('https://apiv2.twitcasting.tv/internships/2019/games/'+id,json.dumps({"answer":my_ans}),headers={"content-type": "application/json",'Authorization': token})
print(response.json())