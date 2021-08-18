
from bottle import *
import pymongo
from pymongo import MongoClient
from bson import ObjectId

db = MongoClient(host='mongodb://localhost', port=27017)
test_db = db.test # select database

@get('/')
def index():
	return template('views/index.html')

@get('/form2')
def index():
	return template('views/index2.html')

@get('/profile')
def index():
	return template('views/profile.html')

@get('/profile/<name>')
def index(name):
	profile = test_db.user_profile.find_one({"username":name})
	
	stock = ['']
	screener_fav = ['']

	return template('views/profile.html', stock=stock, screener_fav=screener_fav, user='admin')

@post('/profile-data')
def profile_data():
	a = test_db.user_profile.find({"name":"Your Name"}) # return pymongo cursor
	a = list(a)  # Cast pymongo cursor to list type
	# a = list(test_db.user_profile.find({"name":"Your Name"}))

	# 0 == False
	# 1 == True

	b = test_db.user_profile.find_one({"name":"Your Name"}) # return dict
	# b = test_db.user_profile.find_one({"name":"Your Name"}, {'_id': False}) # return dict

	# print (a)
	# for u in a:
	# 	print ("First Loop")
	# 	print (u)
	# # b = test_db.user_profile.find_one({""})

	# for u in a:
	# 	print ("Second Loop")
	# 	print (u)
	
	print (b)
	# for u in b:
	# 	print ("First Loop for B")
	# 	print (u)

	# print (b)
	# for u in b:
	# 	print ("Second Loop for B")
	# 	print (u)
	
	# return {
	# 	"name": 'Your Name',
	# 	"gender": 'Alien',
	# 	"age": 119,
	# 	"status": 'Plural',
	# 	"address": 'Pluto'
	# }

	# del b['_id'] # remove key _id

	# Avoid Key Error
	# Cara 1 
	# try:
	# 	del b['test']
	# except:
	# 	pass

	# Cara 2
	# if 'test' in b:
	# 	del b['test']

	#
	# print (b['profile'])

	b['_id'] = str(b['_id']) # cast ObjectId to String

	return b

# Cara 1
@post('/submit-form')
def submit_form():

	data = request.json
	print (data)

	# Insert to database
	test_db.forms.insert_one({
		"email": data.email,
		"password": data.password
	})


	return "Form Success"

# Cara 2
@post('/submit-form')
def submit_form():
	email = request.forms.email
	password = request.forms.password

	print (email)
	print (password)
	
	# Insert to database
	test_db.forms.insert_one({
		"email": email,
		"password": password
	})


	return "Form Success"

@get('/submit-form')
def submit_form():
	email = request.query.email
	password = request.query.get('password')
	print (email)
	print (password)

	# Insert to database
	test_db.forms.insert_one({
		"email": email,
		"password": password
	})


	return "Success"

@get('/update-form/<id>')
def update_form(id):
	id = ObjectId(id)
	form = test_db.forms.find_one({"_id":id})
	# print (id)
	# print (type(id))
	# print (form)
	return template('views/form_update.html', form=form)

@post('/update-form')
def update_form():
	email = request.forms.email
	password = request.forms.password
	id = request.forms.id

	print (email)
	print (password)
	print (id)

	test_db.forms.update_one({"_id": ObjectId(id)}, {"$set": {
		"email": email,
		"password": password,
		"keybaru":"", # set new key
	}})

	redirect('/update-form/'+id)
	# redirect('/update-form/%s' % (id) )

@get('/update-form/delete/<id>')
def delete_form(id):
	test_db.forms.delete_one({"_id":ObjectId(id)})
	return "done"

# # DB operation (CRUD)

# # Create
# test_db.forms.insert_one() # single document
# test_db.forms.insert_many() # many document

# # Read
# test_db.forms.find_one() # single document
# test_db.forms.find() # many document

# # Update
# test_db.forms.update_one({'criteria_key': 'value'}, {"$set": {"key": 'value'}}) # single document
# test_db.forms.update_many({'criteria_key': 'value'}, {"$set": {"key": 'value'}}) # many document

# # Delete Document
# test_db.forms.delete_one() # single document
# test_db.forms.delete_many() # many document

# # Delete Key
# test_db.forms.update_one({'criteria_key': 'value'}, {"$unset": {"key": ''}}) # single document
# test_db.forms.update_many({'criteria_key': 'value'}, {"$unset": {"key": ''}}) # many document


@get('/dashboard')
def test(route='dashboard', type='integer', value="1"):
	return "hi"

@get('/static/<filename:path>') # :path for long path eg. /js/test.js
def serve_js(filename):
	return static_file(filename, 'static')

run(port=4777, reloader=True, debug=True) #port 8080 & 80 utk web
