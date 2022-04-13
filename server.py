from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index(): # 함수 이름은 아무거나 해도 상관 없음
    return 'welcome'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>')
def read(id):
    return 'read '+id


app.run(debug=True) # 실제 서버에서는 디버거 모드로 실행하면 안됨