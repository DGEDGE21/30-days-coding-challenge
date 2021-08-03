from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse


app=Flask(__name__)

@app.route("/")
def hello():
    return "OLa mundoooo"
@app.route("/sms",methods=["POST"])
def sms_reply():
    msg=request.form.get('Body')
    numero=request.form.get('From')
    print(msg)
    resp=MessagingResponse()
    resp.message("ola"+numero)
    return str(numero)

if __name__=="__main__":
     app.run(debug=True)