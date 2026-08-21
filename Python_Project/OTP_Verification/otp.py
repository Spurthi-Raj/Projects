from flask import Flask,render_template,request, session
from twilio.rest import Client
import random

app = Flask(__name__)
app.secret_key = 'otp'

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/getOTP', methods=['POST'])
def getOTP():
    number = request.form['number']
    val = getOPTApi(number)
    if val:
        return render_template('enterOTP.html')

def generateOTP():
    return random.randrange(100000,999999)


@app.route('/validateOTP', methods=['POST'])
def validateOTP():
    otp = request.form['otp']
    if 'response' in session:
        s = session['response']
        session.pop('response',None)
        if s == otp:
            return 'You Are Authorized,Thank You'
        else:
            return 'You Are Not Authorized'


def getOPTApi(number):
    account_sid = 'ACe740cba0a0d716003df99bd48c59206c'
    auth_token = '0effea31a7f5cf1c6bd0e4afa67108f1'
    client = Client(account_sid,auth_token)
    otp = generateOTP()
    session['response'] = str(otp)
    body = 'your OTP is '+str(otp)
    message = client.messages.create(from_ = '+12293215771',body=body,to=number)
    if message.sid:
        return True
    else:
        return False

   


if __name__ == '__main__':
    app.run(debug=True)

