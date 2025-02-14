from flask import Flask, request, jsonify

app = Flask(__name__)

# In-Memory "Datenbank" mit vordefiniertem Produkt
products = [
    {"id": 1, "name": "laptop", "price": 1200},
    {"id": 2, "name": "tv", "price": 800},
    {"id": 3, "name": "laptop", "price": 1200},
    {"id": 4, "name": "tv", "price": 1200},
    {"id": 5, "name": "laptop", "price": 1200},
]


# http://127.0.0.1:6060/products ???
@app.route("/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    if not new_product or "name" not in new_product or "price" not in new_product:
        return jsonify({"error": "Invalid input"}), 400

    new_product["id"] = max([p["id"] for p in products], default=0) + 1
    products.append(new_product)
    return jsonify(new_product), 201


# http://127.0.0.1:6060/products?name=laptop
@app.route("/products", methods=["GET"])
def get_products():
    name_filter = request.args.get("name") # ← macht das ?name=<product>
    if name_filter:
        filtered_products = [
            p for p in products if name_filter.lower() in p["name"].lower()
        ]
        return jsonify(filtered_products), 200
    return jsonify(products), 200


if __name__ == "__main__":
    app.run(port=6060, debug=True)
