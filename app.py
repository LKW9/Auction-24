from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.r95aysd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
id='abcd'

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

@app.route('/upload', methods=["GET"])
def upload():
    return render_template('/upload.html')

###MAIN###
@app.route("/items", methods=["GET"])
def getItemList():
    allItems = list(db.items.find({}))
    return jsonify({'allItems': allItems})


##Upload##
@app.route("/upload" , methods=["POST"])
def uploadItem():
    itemList = list(db.bucket.find({}, {'_id': False}))
    itemNum = len(itemList) + 1
    title = request.form['title']
    pic = request.form['pic']
    minBid = request.form['minBid']
    nowBid = request.form['nowBid']
    unitBid = request.form['unitBid']
    desc = request.form['desc']
    status = request.form['status']
    owner = id
    item = {
        'itemNum' : itemNum,
        'title' : title,
        'pic' : pic,
        'minBid' : minBid,
        'nowBid' : nowBid,
        'unitBid' : unitBid,
        'status' : status,
        'desc' : desc,
        'owner' : owner
    }
    db.items.insert_one(item)
    return jsonify({'msg' : '등록되었습니다.'})


###Modify page###
@app.route('/detail/<int:id>')
def detail(id):

    return render_template('/detail.html',id=id)









if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)