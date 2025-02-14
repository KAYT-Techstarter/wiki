from flask import Flask, request, jsonify

app = Flask(__name__)

# http://127.0.0.1:5000/brand/21?type=clothes&condition=new
@app.route('/brand/<id>')
def brand(id):
    type_ = request.args.get('type')
    condition = request.args.get('condition')
    return f"Brand-ID: {id}, Type: {type_}, Condition: {condition}"

# http://127.0.0.1:5000/product/2123
@app.route('/product/<product_id>')
def product(product_id):
    return f"Product-ID: {product_id}"

# http://127.0.0.1:5000/search?query=black
@app.route('/search')
def search():
    query = request.args.get('query')
    return f"Searching for: {query}"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
