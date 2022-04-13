from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>' + str(random.random()) + '</strong>'

app.run(debug=True) # 실제 서버에서는 디버거 모드로 실행하면 안됨