from datetime import datetime

from flask import render_template, request

from core import app

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route ('/create_post', methods = ['POST', 'GET'] )
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('title')
        with open ('data.txt' , 'w', encoding = 'utf-8') as f:
            data = {
                'title': title,
                'description': description,
                'date': datetime.now()
            }
            f.write (str (data) + '\n')
    return render_template ('create_post.html')

@app.route ('/signup',methods = ['POST', 'GET'])
def signup():
    return render_template('signup.html')