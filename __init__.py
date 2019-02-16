from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api, reqparse
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
		args = parser.parse_args()
		grid = args['grid']

		resp = {}
		resp['grid'] = grid
		resp['winner'] = ''

		#Check for winner
		winner = ttt.checkWinner(grid)

		# If there is a winner, return response
		if winner != '':
			resp['winner'] = winner

		# Otherwise, make a move
		else:
			for i in range(len(grid)):
				if(grid[i] == ' '):
					grid[i] = 'O'
					break

			resp['winner'] = ttt.checkWinner(grid)
		
		return resp


api.add_resource(HelloWorld, '/')
api.add_resource(NameDate, '/ttt/')
api.add_resource(MakeMove, '/ttt/play')


if __name__ == '__main__':
    app.run(debug=True)