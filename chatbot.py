from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from tap import get_relevant

app=Flask(__name__)

@app.route("/")

def hello():
    return "OLa mundoooo"
@app.route("/sms",methods=["POST"])
def sms_reply():
    res=MessagingResponse()
    if request.form['NumMedia']!='0':
        image_url=request.form['MediaUrl0']
        relevant_tags=get_relevant(image_url)
        res.message('\n'.join(relevant_tags ))
    else:
        res.message("por favor envie uma imagem")

    return str(res)

if __name__=="__main__":
     app.run(debug=True)