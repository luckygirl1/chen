from flask import Blueprint
talk_=Blueprint('talk_',__name__)
@talk_.route('/talk',methods=(['POST']))
def talk():
    return ('thank you')
