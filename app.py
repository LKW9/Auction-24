from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.r95aysd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

###HOME###
@app.route('/')
def home():
    ##jwt 인증 토큰이 없으면 로그인 페이지 렌더링
    ##jwt 인증 토큰이 있으면 main 렌더링
    return render_template('main.html')

###AUTH###
@app.route('/auth/login')
def login():
    return render_template('/auth/login.html')

@app.route('/auth/join')
def join():
    return render_template('/auth/join.html')

###MAIN###
@app.route("/items", methods=["GET"])
def getItemList():
    users = db.users.find({})
    allItems = []
    for user in users:
        items = user['items']
        for num in range(len(items)):
            allItems.append(items[num])
    return jsonify({'allItems': allItems})



###Modify page###
@app.route('/detail/<int:id>')
def detail(id):

    return render_template('/detail.html',id=id)


##item upload##
@app.route("/users/<id>/items",methods=["POST"])
def uploadItem(id):
    items = db.users.find_one({'id':id})['items']
    title = request.form['title']
    pic = request.form['pic']
    minBid = request.form['minBid']
    unitBid = request.form['unitBid']
    desc = request.form['desc']
    status = request.form['status']
    owner = id
    num = len(items) + 1
    item = {
        'itemNum' : num+1,
        'title' : title,
        'pic' : pic,
        'minBid' : minBid,
        'unitBid' : unitBid,
        'status' : status,
        'desc' : desc,
        'owner' : owner
    }
    items.append(item)
    db.users.update_one({'id': id}, {'$set': {'items': items}})
    return jsonify({'msg' : '등록 완료!'})









if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)