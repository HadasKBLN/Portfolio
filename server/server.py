from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/person/<string:id>', methods=['POST'])
def new_contact(id):
    print(id)
    return 'new contact created!'

@app.route('/person/<string:id>', methods=['PUT'])
def new_contact(id):
    print(id)
    return 'new contact created!'

@app.route('/person/<string:id>', methods=['DELETE'])
def new_contact(id):
    print(id)
    return 'new contact created!'

@app.route('/person', methods=['GET'])
def get_contacts():
    return 'All the IDs!'

@app.route('/person/<string:person_id>', methods=['GET'])
def get_person(id):
    return 'All the IDs!'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')