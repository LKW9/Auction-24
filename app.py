from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.r95aysd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/auth/login')
def login():
    return render_template('/auth/login.html')

@app.route('/auth/join')
def join():
    return render_template('/auth/join.html')

@app.route('/detail/<int:id>')
def detail(id):
    return render_template('/detail.html',id=id)



@app.route("/home", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_list = list(db.bucket.find({}, {'_id' : False}))
    count = len(bucket_list) + 1

    doc = {
        'title'
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': 'POST(기록) 연결 완료!'})

@app.route("/home", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})


##item upload##
@app.route("/users/<id>/items",methods=["POST"])
def uploadItem(id):
    items = db.users.find_one({'id':id})['items']
    title = request.form['title']
    pic = request.form['pic']
    minBid = request.form['minBid']
    desc = request.form['desc']
    status = request.form['status']
    num = len(items) + 1
    item = {
        'itemNum' : num+1,
        'title' : title,
        'pic' : pic,
        'minBid' : minBid,
        'status' : status,
        'desc' : desc
    }
    items.append(item)
    db.users.update_one({'id': id}, {'$set': {'items': items}})
    return jsonify({'msg' : '등록 완료!'})

### 안녕하세요 김머현입니다###







if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)