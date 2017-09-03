#coding:utf-8
from flask import Flask,render_template
from models import User
app = Flask(__name__)


@app.route('/')
def hello_world():
    content = 'show webInfo'
    return render_template('index.html',content=content)


@app.route('/user')
def showUser():
    user = User('1929','hundredOne')
    return render_template('indexUser.html',user=user)

@app.route('/userQuery/<show_id>')
def showUserQuery(show_id):
    user = None
    # 注意中文的处理
    if int(show_id) == 1:
        user = User(1,'ShowRight')

    return render_template('indexUser.html',user = user)


@app.route('/userId/<show_id>')
def showUserID(show_id):
    user = None
    if  int(show_id) ==1:
        user = User(1,'firstUser')
    return  render_template('user_id.html',user=user)

@app.route('/userList')
def showUserList():
    users = []
    for i in range(1,11):
        user = User(i,'Client:%d'%i)
        users.append(user)
    return render_template('user_idList.html',users=users)

@app.route('/one')
def showOne():
    return render_template('one_base.html')

@app.route('/two')
def showTwo():
    return render_template('two_base.html');

if __name__ == '__main__':
    app.run()
