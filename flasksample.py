from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import datetime

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


api.add_resource(HelloWorld, '/')
api.add_resource(NameDate, '/ttt/')


if __name__ == '__main__':
    app.run(debug=True)