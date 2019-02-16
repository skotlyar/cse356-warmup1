from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api, reqparse
import datetime
import sys

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class NameDate(Resource):
	def post(self):
		headers = {'Content-Type': 'text/html'}
		name = request.form['name']
		now = datetime.datetime.now()
		date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
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
		# grid = request.form['grid']
		parser = reqparse.RequestParser()
		parser.add_argument('grid', action='append')
		args = parser.parse_args()
		grid = args['grid']
		print(str(grid) + "##############################", file=sys.stderr)
		# print(str(request['grid']) + "##############################", file=sys.stderr)

		for i in range(len(grid)):
			if(grid[i] == ' '):
				grid[i] = 'O'
				break
		resp = {}
		resp['grid'] = grid
		resp['winner'] = ''
		return resp


api.add_resource(HelloWorld, '/')
api.add_resource(NameDate, '/ttt/')
api.add_resource(MakeMove, '/ttt/play')


if __name__ == '__main__':
    app.run(debug=True)