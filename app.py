from flask import Flask, session, render_template, request, jsonify

import requests



from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.r95aysd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)
app.secret_key = "Mykey"

sessionId = 0

# API
# CONSTANT
REQ = {
    'KEY': 'User-Agent',
    'VALUE': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

###Sessions###
def checkSessionValidation():
  if session['id']:
    global sessionId;
    sessionId = session['id']
    return
  return render_template('/auth/login.html')


###HOME###
@app.route('/')
def home():
    if 'id' in session:
        global sessionId
        print(sessionId)
        return render_template('main.html')
    else:
        print(sessionId)
        return render_template('/auth/login.html')

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

###AUTH###
@app.route('/auth/login', methods=['GET'])
def getlogin():
    return render_template('/auth/login.html')


@app.route('/auth/login', methods=['POST'])
def logIn():
    user_id = request.form['inputId']
    user_pw = request.form['inputPw']
    error = True
    # 유효성 검사 (빈문자열, 4자리 미만, ID 존재여부 -> 존재하면 PW 일치 확인)
    if (len(user_id.strip()) == 0):
        msg = "ID를 입력해 주세요."
    elif (len(user_pw.strip()) == 0):
        msg = "PW를 입력해 주세요."
    elif (len(user_id) < 4 or len(user_pw) < 4):
        msg = "ID와 PW의 길이는 4자가 넘어야 합니다."
    elif (db.users.find_one({'id': user_id}) == None):  # 등록되지 않은 ID
        msg = "등록되지 않은 ID입니다. 회원가입 하세요."
    elif (db.users.find_one({'id': user_id})['pw'] != user_pw):  # ID, PW 일치 확인
        msg = "ID와 PW가 일치하지 않습니다. 다시 확인해보세요."
    else:
        msg = "로그인 성공"
        error = False  # 로그인 가능
        session['id'] = user_id
        global sessionId
        sessionId = user_id

    return jsonify({'message': msg, 'error': error})

@app.route('/auth/join', methods=['GET'])
def join():
    return render_template('/auth/join.html')

@app.route('/auth/signIn', methods=['POST'])
def signIn():
    inputId = request.form['inputId']
    inputPw = request.form['inputPw']
    inputName = request.form['inputName']
    error = True
    # 유효성 검사 (빈문자열, 4자리 미만, ID중복 여부)
    if (len(inputId.strip()) == 0):
        msg = "ID를 입력해 주세요."
    elif (len(inputPw.strip()) == 0):
        msg = "PW를 입력해 주세요."
    elif (len(inputId) < 4 or len(inputPw) < 4):
        msg = "ID와 PW의 길이는 4자가 넘어야 합니다."
    elif (db.users.find_one({'id': inputId}) != None):  # 이미 등록된 ID
        msg = "이미 등록된 ID라니까요."
    else:
        msg = "회원가입 완료!"
        error = False
        db.users.insert_one({'id': inputId, 'pw': inputPw, 'name': inputName})
    return jsonify({'message': msg, 'error': error})

@app.route('/auth/join/check', methods=['POST'])
def idCheck():
    inputId = request.form['inputId']
    error = True
    if (db.users.find_one({'id': inputId}) != None):
        msg = "중복된 ID입니다."
    else:
        msg = "가입이 가능한 ID입니다."
        error = False
    return jsonify({'message':msg, 'error':error})

#Logout
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('id', None)
    return jsonify({'message': "로그아웃 하셨습니다."})

@app.route('/upload', methods=["GET"])
def upload():
    return render_template('/upload.html')

@app.route('/myPage')
def myPage():
    return render_template('/myPage.html')

###MAIN###
@app.route("/items", methods=["GET"])
def getItemList():
    allItems = list(db.items.find({}))
    return jsonify({'allItems': allItems})


##Upload##
@app.route("/upload" , methods=["POST"])
def uploadItem():
    checkSessionValidation()
    itemList = list(db.bucket.find({}, {'_id': False}))
    itemNum = len(itemList) + 1
    title = request.form['title']
    pic = request.form['pic']
    minBid = request.form['minBid']
    nowBid = request.form['nowBid']
    unitBid = request.form['unitBid']
    desc = request.form['desc']
    status = request.form['status']
    owner = sessionId
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


@app.route('/detail', methods=["POST"])
def bid():
    nowBid_receive = request.form('nowBid_give')
    db.items.insert_one({'nowBid': nowBid_receive})
    return jsonify({'msg': '저장 완료!'})

@app.route('/detail', methods=["GET"])
def bid_list():
    bid_list = list(db.items.find({}, {'_id': False}))
    return jsonify({'bid_list': bid_list})

@app.route('/detail', methods=["POST"])
def bid_fail():

    
    return jsonify({'msg': ' 안돼! '})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)