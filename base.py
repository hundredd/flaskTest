#coding:utf-8
from flask import Flask,request,url_for
app = Flask(__name__)
@app.route('/')
def index():
	return 'hello world' 

@app.route('/user',methods=['POST'])
def showUser():
	return 'hello user'

@app.route('/user/<id>',methods=['POST'])
def showID(id):
	return 'hello user'+id


@app.route('/query', methods=['POST'])
def showHun():
	id = request.args.get('id')
	return 'query' + id

@app.route('/queryPost', methods=['POST'])
def showHunId():
	id = request.args.get('id')
	return 'query' + id

@app.route('/queryUrlFor', methods=['POST'])
# fanxiangluyou
def showQueryUrlFor():
	return 'query url:/t ' + url_for('showHunId')#这里用的是这个路由的函数

if __name__ == '__main__':
	app.run('0.0.0.0')
