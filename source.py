from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'e_store'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/e_store'
mongo = PyMongo(app)


@app.route('/', methods=['POST'])  # add new merchandise
def add_merch():
    merch = mongo.db.merchandise

    # merchandise's fields

    name = request.json['name']
    description = request.json['description']
    specification = request.json['specification']

    merch_id = merch.insert({'name': name, 'description': description, 'specification': specification})
    new_merch = merch.find_one({'_id': merch_id})

    output = {'_id': str(merch_id), 'name': new_merch['name'], 'description': new_merch['description'],
              'specification': new_merch['specification']}

    return jsonify(output)


@app.route('/find', methods=['GET'])  # get merch by name and/or specification
def get_merch_by_name_spec():
    merch = mongo.db.merchandise

    output = []
    name = k = v = ''

    if request.args:
        args = request.args

        # getting query string args
        if 'name' in args:
            name = args['name']
        if 'spec' in args:
            k, v = args['spec'].split('_')

        # find by name and spec feature
        if name and k and v:
            results = merch.find({'name': name, 'specification.{}'.format(k): v})

        # find by spec feature
        elif k and v:
            results = merch.find({'specification.{}'.format(k): v})

        # find by name
        else:
            results = merch.find({'name': name})

        if results:
            for result in results:
                output.append({'_id': str(result['_id']), 'name': result['name']})
        else:
            output = 'No results found'
    else:
        return jsonify({'No query string received'})

    return jsonify(output)


@app.route('/<merch_id>', methods=['GET'])  # get merch by ID
def get_merch_by_id(merch_id):
    merch = mongo.db.merchandise

    query = merch.find_one({'_id': ObjectId(merch_id)})

    if query:
        output = {'_id': merch_id, 'name': query['name'], 'description': query['description'],
                  'specification': query['specification']}
    else:
        output = 'No such ID'

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=False)
