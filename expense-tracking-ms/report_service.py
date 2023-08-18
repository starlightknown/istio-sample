from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

expenses = []

@app.route('/report', methods=['GET'])
def generate_report():
    total_expenses = sum(expense['amount'] for expense in expenses)
    return jsonify({'total_expenses': total_expenses})

if __name__ == '__main__':
    app.run(port=3004)
