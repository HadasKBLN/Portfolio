from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json
from flask import render_template


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'contactdb'

app.config["MONGO_URI"] = "mongodb://admin:password@mongodb:27017/contactdb"
mongodb_client = PyMongo(app)
db = mongodb_client.db
   

# Add a new contact
@app.route('/person/<string:id>', methods=['POST'])
def add_contact(id):
    if not request.json or not 'name' in request.json or not 'number' in request.json or not 'city' in request.json:
        return jsonify(message="Some details are missing. Fill them and try again.")
    contact = db.contacts.find_one({"id": id})
    if contact:
        return jsonify(message="Contact with such ID already exist")
    db.contacts.insert_one({'id': id, 'name': request.json['name'], 'number':request.json['number'], 'city': request.json['city']})
    return jsonify(message="New contact added succesfully!")

# Update an existing contact
@app.route('/person/<string:id>', methods=['PUT'])
def update_contact(id):
    contact = db.contacts.find_one({'id': id})
    updated_contact = {}
    if contact:
        updated_contact['id'] = contact['id']
        if 'name' in request.json:
            updated_contact['name'] = request.json['name']
        else:
            updated_contact['name'] = contact['name']

        if 'number' in request.json:
            updated_contact['number'] = request.json['number']
        else:
            updated_contact['number'] = contact["number"]

        if 'city' in request.json:
            updated_contact['city'] = request.json['city']
        else:
            updated_contact['city'] = contact['city']
    
        result = db.contacts.replace_one({'id': id}, updated_contact)
        return jsonify(massage="Contact updated succesfully")
    else:
        return jsonify(massage="No such contact. Enter id again")


# Delete an existing contact
@app.route('/person/<string:id>', methods=['DELETE'])
def delete_contact(id):
    contact = db.contacts.find({'id': id})
    if contact:
        deleted_contact = db.contacts.delete_one({'id': id})
        return jsonify(massage="Contact deletes succesfully")
    else:
        return jsonify(massage="Contact with such ID is not exist") 


# Get all contacts
@app.route('/person', methods=['GET'])
def get_all_contacts():
    contacts = db.contacts.find()
    contacts_list = []
    for contact in contacts:
        contacts_list.append(JSONEncoder().encode(contact))
    return jsonify(contacts_list)


# Get contact with a given ID
@app.route('/person/<string:id>', methods=['GET'])
def get_person(id):
    contact = db.contacts.find_one({"id": id})
    if contact:
        return JSONEncoder().encode(contact)
    else:
        return jsonify(massage="Contact with such ID is not exist")


# Welcome
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')