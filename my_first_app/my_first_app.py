# This is whre you can start you python file for your week1 web app
# Name: Alex Choi

import flask, flask.views
import os
app = flask.Flask(__name__)
#Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
#What is MethodView?
#Is this the class that allows me to actually view something in the browser?
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		result = eval(flask.request.form['expression'])
		#Why did I have it run eval on this line of code?
		flask.flash(result)
		return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()