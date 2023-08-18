from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

categories = []

@app.route('/categories', methods=['POST'])
def add_category():
    category = request.json
    categories.append(category)
    return jsonify(category), 201

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

if __name__ == '__main__':
    app.run(port=3003)
