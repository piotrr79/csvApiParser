from flask import Flask, jsonify, request, abort

# Initialize Flask application
app = Flask(__name__)
app.config['DEBUG'] = False

def __init__(self):
    self

@app.errorhandler(404)
def page_not_found(error):
    return "404", 404

@app.route('/api-success', methods=['GET'])
def success():
    """ Return success api response with list of accounts"""
    return jsonify(
            {'count':22,'next': 'null','previous': 'null','results':[
                {'account_id': 12345, 'status': 'good', 'created_on': '2011-01-12'},
                {'account_id': 271, 'status': 'good', 'created_on': '2011-03-22'},
                {'account_id': 8675309, 'status': 'closed', 'created_on': '014-12-21'},
                {'account_id': 99999, 'status': 'fraud', 'created_on': '2014-09-17'},
                {'account_id': 8172, 'status': 'closed', 'created_on': '2015-09-01'},
                {'account_id':1924,'status':'fraud','created_on':'2012-03-01'},
                {'account_id':222222,'status':'poor','created_on':'2014-01-02'},
                {'account_id':666,'status':'high risk','created_on':'2015-04-01'},
                {'account_id':48213,'status':'high risk','created_on':'2015-08-15'},
                {'account_id':918299,'status':'good','created_on':'2014-06-01'},
                {'account_id':88888,'status':'collections','created_on':'2015-08-08'},
                {'account_id':99,'status':'good','created_on':'2012-01-12'},
                {'account_id':798979,'status':'good','created_on':'2012-01-12'},
                {'account_id':0,'status':'good','created_on':'2012-01-12'},
                {'account_id':27,'status':'awesome','created_on':'2012-01-12'},
                {'account_id':7,'status':'awesome','created_on':'2012-01-12'},
                {'account_id':272727,'status':'awesome','created_on':'2020-10-19'},
                {'account_id':200,'status':'awesome','created_on':'2020-10-10'},
                {'account_id':201,'status':'awesome','created_on':'2020-10-10'}
            ]}
        )

@app.route('/api-error', methods=['GET'])
def error():
    """ Return error api response """
    abort(404)
    return 'Not Found'

app.run()