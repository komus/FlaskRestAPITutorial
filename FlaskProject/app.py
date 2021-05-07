from flask import Flask, jsonify, request

app = Flask(__name__)

stores =[
    {
        'name':'Just a store',
        'items':[
                {
                   'name':'Store item1',
                   'price':5.99
                }
            ]
    }
   ]

#POST /store data:{storename}
@app.route("/store", methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items':[]
        }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


 #GET /store
@app.route("/store")
def get_stores():
     return jsonify({'stores':stores})


#POST /store/<string:name>/item data:{storename}
@app.route("/store/<string:name>/item", methods = ['POST'])
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['item'],
                'price': request_data['price']
                }
            store['items'].append(new_item)
            return jsonify({'item': new_item})
    return jsonify({'message': "No store info"})
            

#POST /store/<string:name>/item data:{storename}
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores: 
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})



app.run(port = 5000)
       