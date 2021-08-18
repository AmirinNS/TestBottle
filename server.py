from bottle import *

# from bottle import Bottle, route, get, post, template, default_app, run


app_main = Bottle()
app2 = Bottle()
app3 = Bottle()

@app_main.route('/')
def main():
	return 'index'

@app_main.route('/test')
def test():
	return "1234"

@app2.route('/')
def main():
	return 'index 2'

@app2.route('/test')
def test():
	return {'test': 'test'}

@app3.route('/')
def main():
	return 'index 3'

@app3.route('/udin')
def test():
	return {'nwar': 'have number'}

# Run server

app_main.mount("/forum ", app2)
app_main.mount("/dashboard", app3)


run(app=app_main, port=1234)

