import json
with open('routes.json','r',encoding='utf-8-sig') as f:
    JsonFile=json.load(f)
Number=len(JsonFile['food_name'])
ans=[]
for i in range(Number):
    temp={}
    temp['food_name']=JsonFile['food_name'][i]
    temp['routes']=JsonFile['routes'][i]
    temp['time']=JsonFile['time'][i]
    temp['is_safe']=JsonFile['is_safe'][i]
    temp['food_url']=JsonFile['food_url'][i]
    temp['describe']=JsonFile['describe'][i]
    ans.append(temp)
ans=json.dumps(ans,ensure_ascii=False)
print(ans)
