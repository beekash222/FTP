import pandas as pd
from flask_cors import CORS
import flask
from flask import Flask, request,render_template

app = Flask(__name__)
CORS(app)

app=flask.Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
    NID = request.form['NID']
    USERNAME = request.form['USERNAME']
    password = request.form['password']
    w3mission4 = request.form['message1']
    NID1 = request.form['NID1']
    USERNAME1 = request.form['USERNAME1']
    password1 = request.form['password1']
    if 'create_draft' in request.form:
            x= w3mission4
    elif 'create_post' in request.form:
            x= "Mohanty"
    return render_template('main.html', prediction_text=x)


if __name__=="__main__":
    #port=int(os.environ.get('PORT',33507))
    app.run(debug=True,use_reloader=False)

    #host='0.0.0.0',0.0.0.0
