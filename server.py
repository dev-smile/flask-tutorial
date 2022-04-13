from flask import Flask
import random

app = Flask(__name__)

topics = [ # 실제로는 여기에 DB를 읽어오는 부분을 작성
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''

def getContents():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
    

@app.route('/')
def index(): # 함수 이름은 아무거나 해도 상관 없음
    liTags = ''
    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    return template(liTags, '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')


@app.route('/create/')
def create():
    return 'Create'


app.run(debug=True) # 실제 서버에서는 디버거 모드로 실행하면 안됨