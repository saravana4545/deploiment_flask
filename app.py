from flask import Flask, request,session, render_template, redirect, url_for
#import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        session['user_name'] = request.form['user_name']
        session['password']  = request.form['password']

        return redirect(url_for('result'))
    return render_template('index.html', show = None)

@app.route('/datas')
def result():
    user1 = session.get('user_name')
    user2 = session.get('password')
    data1 = user1
    data2 = user2
    
    #print(f'get values{values}')
    return render_template('webpage.html', item1=data1, item2=data2)
    
#def startpy():
#    result()

if __name__ == '__main__':
    app.run(debug=True)