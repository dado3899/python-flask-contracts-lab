#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response


contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<id>')
def contract(id):
    for contract in contracts :
        if contract["id"] == int(id):
            response_body = contract["contract_information"]
            status_code = 200
            headers = {}
            return make_response(response_body, status_code, headers)
    response_body = ""
    status_code = 404
    headers = {}
    return make_response(response_body, status_code, headers)

@app.route('/customer/<name>')
def customer(name):
    if name in customers:
        response_body = ""
        status_code = 204
        headers = {}
        return make_response(response_body, status_code, headers)
    else:
        response_body = ""
        status_code = 404
        headers = {}
        return make_response(response_body, status_code, headers)




if __name__ == '__main__':
    app.run(port=5555, debug=True)
