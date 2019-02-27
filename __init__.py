from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api, reqparse
import pymongo
import datetime
import sys
import tttalgorithm as ttt

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class NameDate(Resource):
	def post(self):
		headers = {'Content-Type': 'text/html'}
		name = request.form['name']
		# Format the date
		now = datetime.datetime.now()
		month =str(now.month) if len(str(now.month)) == 2 else '0' + str(now.month)
		day =str(now.day) if len(str(now.day)) == 2 else '0' + str(now.day)
		date = str(now.year) + '-' + month + '-' + day
		stuff = {'name': name, 'date': date}
		return make_response(render_template('index.html', stuff = stuff),200,headers)
	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template('home.html'),200,headers)

class MakeMove(Resource):
	def post(self):
		# Check winner
		# Choose move
		# Check winner
		# Return updated JSON
		# Parse arguments from server
		parser = reqparse.RequestParser()
		parser.add_argument('grid', action='append')
		parser.add_argument('model', action='append')
		args = parser.parse_args()
		grid = args['grid']
		model = []
		for i in grid:
			if i == 'X':
				model.append(1)
			elif i == 'O':
				model.append(-1)
			else:
				model.append(0)
		resp = {}
		resp['grid'] = grid
		resp['winner'] = ''
		#Check for winner
		winner = ttt.checkWinner(model)
		# If there is a winner, return response
		if winner != '':
			resp['winner'] = winner
		# Otherwise, make a move
		else:
			move = ttt.makeMove(model)
			grid[move] = 'O'
			model[move] = -1
			resp['winner'] = ttt.checkWinner(model)
		# print('#######################model:' + str(model), file=sys.stderr)
		return resp

class AddUser(Resource):
	def post(self):
		# TODO make try catch, return success or failure in json format
		parser = reqparse.RequestParser()
		parser.add_argument('username')
		parser.add_argument('password')
		parser.add_argument('email')
		args = parser.parse_args()
		username = args['username']
		password = args['password']
		email = args['email']
		myclient = pymongo.MongoClient('mongodb://130.245.170.88:27017/')
		mydb = myclient['warmup2']
		fb = mydb['users']

		user = {}
		user['username'] = username
		user['password'] = password
		user['email'] = email
		user['enabled'] = False

		#Generate email verification code

		fb.insert(user)
class Verify(Resource):
	def post(self):



api.add_resource(HelloWorld, '/')
api.add_resource(NameDate, '/ttt/')
api.add_resource(MakeMove, '/ttt/play')
api.add_resource(AddUser, '/adduser')



if __name__ == '__main__':
    app.run(debug=True)
