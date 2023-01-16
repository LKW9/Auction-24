from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('몽고 주소')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/home", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_list = list(db.bucket.find({}, {'_id' : False}))
    count = len(bucket_list) + 1

    doc = {
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': 'POST(기록) 연결 완료!'})

@app.route("/home", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)