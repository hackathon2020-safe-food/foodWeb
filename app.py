from flask import Flask, request, json, jsonify,redirect,url_for
from flask import render_template

app = Flask(__name__)
import os
import sys

work_dir = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "./demo/"))
print(work_dir)
sys.path.append(work_dir)
now_dir = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "./foodWeb/"))
print(now_dir)
sys.path.append(now_dir)
from route_display import MapAndRoute
print(work_dir)


@app.route('/')
def hello_world():
    print("hello world")
    return render_template('index.html')


@app.route('/goodsInfo/', methods=['POST'])
def goodsInfo():
    with open(work_dir+'/res.json', 'r', encoding='utf-8-sig') as f:
         CountryBorder= json.load(f)
    result=CountryBorder
    print("goodsInfo")
    return jsonify({'status': '1', 'result': result}), 200, {"ContentType": "application/json"}


@app.route('/goods/<name>',methods=['POST','GET'])
def getMap(name):
    if request.method=='GET':
        with open(work_dir + '/res.json', 'r', encoding='utf-8-sig') as f:
            CountryBorder = json.load(f)
        result = CountryBorder
        for i in result:
            if i['food_name']==name:
                print(i)
                route=i['routes']
                time=i['time']
                break
        parm = []
        parm.append(name)
        parm.append(route)
        parm.append(time)
        map = MapAndRoute(parm)
        path = now_dir + '/templates/route_display.html'
        map.save(path)
        return render_template('route_display.html')
    route=request.json["route"]
    time=request.json['time']
    print(route)
    print(time)
    parm=[]
    parm.append(name)
    parm.append(route)
    parm.append(time)
    map=MapAndRoute(parm)
    print("goods")
    path=now_dir+'/templates/route_display.html'
    map.save(path)
    print("save")
    return jsonify({'status': '1'}), 200, {"ContentType": "application/json"}
    #return render_template('route_display.html')

@app.route('/goods/show')
def show():
    return render_template('route_display.html')

if __name__ == '__main__':
    app.run(host="192.168.2.169",debug=True)
