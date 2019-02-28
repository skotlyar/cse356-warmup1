from flask import Flask, request, render_template, make_response, jsonify
from flask_restful import Resource, Api, reqparse
import pymongo
import datetime
import sys
import tttalgorithm as ttt
import smtplib, ssl
import string
import random
app = Flask(__name__)
api = Api(app)

class Homepage(Resource):
	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template('signup.html'),200,headers)


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
		try:
			args = parse_args_list(['username', 'password', 'email'])
			username = args['username']
			password = args['password']
			email = args['email']
			users = get_users_coll()
			user = {}
			user['username'] = username
			user['password'] = password
			user['email'] = email
			user['verification'] = generate_code()
			user['enabled'] = False

			if users.find({"username":username}).count() > 0:
				return {"status":"ERROR", "message":"The requested username has already been taken."}

			if users.find({"email":email}).count() > 0:
				return {"status":"ERROR", "message":"The requested email has already been taken."}

			url = 'http://localhost:5000/verify?email=' + email + '&key=' + user['verification']
			message = 'Subject: Verify Your Email\n\n Click here to verify your email\n' + url
			send_email(email, message)
			users.insert(user)
			return {"status":"OK"}
		except Exception as e:
			return {"status":"ERROR"}
class Verify(Resource):
	def post(self):
		try:
			self.handleRequest(parse_args_list(['email', 'key']))
			return {"status":"OK"}
		except Exception as e:
			return {"status": "ERROR"}
	def get(self):
		# TODO, have this return html saying "your account is verified" instead of this json
		# OK or ERROR JSON should only be returned by POST, not GET
		try:
			self.handleRequest(request.args)
			return {"status":"OK"}
		except Exception as e:
			return {"status": "ERROR"}
	def handleRequest(self, args):
		# args = parse_args_list(['email', 'key'])
		email = args['email']
		key = args['key']
		users = get_users_coll()
		user = users.find_one({"email":email})

		if user['verification'] == key or user['verification'] == 'abracadabra':
			users.update_one({"email":email}, {"$set":{"enabled":True}})

class Login(Resource):

	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template('login.html'),200,headers)
	def post(self):
		headers = {'Content-Type': 'application/json'}
		response = make_response(jsonify({"status": "OK"}), 200, headers)
		response.set_cookie('username', '22')
		return response
		


def send_email(receiver, message):
	port = 465  # For SSL
	password = "W2v0&lkde"
	# Create a secure SSL context
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("ljkasdfoir21395@gmail.com", password)
		# TODO: Send email here
		server.sendmail("ljkasdfoir21395@gmail.com", receiver, message)

def parse_args_list(argnames):
	parser = reqparse.RequestParser()
	for arg in argnames:
		parser.add_argument(arg)
	args = parser.parse_args()
	return args

def get_users_coll():
	myclient = pymongo.MongoClient('mongodb://130.245.170.88:27017/')
	mydb = myclient['warmup2']
	users = mydb['users']
	return users
		

def generate_code():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


api.add_resource(Homepage, '/')
api.add_resource(NameDate, '/ttt/')
api.add_resource(MakeMove, '/ttt/play')
api.add_resource(AddUser, '/adduser')
api.add_resource(Verify, '/verify')
api.add_resource(Login, '/login')



if __name__ == '__main__':
	app.run(debug=True)
