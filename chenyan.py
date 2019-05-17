from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager, create_access_token
import ok.talks
class User():
    def __init__(self,username,password):
        self.username = username
        self.password = password
app = Flask(__name__)
app.config['JWT_CRECT_KEY ']='super-crect'
jwt=  JWTManager(app)
app.register_blueprint(ok.talks.talk_)
users = {}
@app.route('/signup',methods=(['POST']))
def sigup():
    if not request.is_json:
        return({'msg':"missing json in request"}),400
    username = request.json.get('username',None)
    password = request.json.get('password',None)
    if not username:
        return jsonify({"msg":"missing username"}),400
    if not password:
        return jsonify({"msg": "missing password"}), 400
    users[username]=User(username,password)
    return jsonify({"msg":"Signup success"}),200
@app.route('/login',methods=(['POST']))
def login():
    if not request.is_json:
        return ({'msg': "missing json in request"})
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username) or (not password):
        return jsonify({"msg":"missing username or password"})
    loginuser = users.get(username,None)
    if not loginuser:
        return({"msg":"User not exit"}),401
    if loginuser and loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username)),200
    else:
        return jsonify({"msg":"usernmae or password incorrect"}),401
    test.route('/say', methods=(['POST']))

if __name__=='__main__':
    app.run(port = 5002)





