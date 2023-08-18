from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
expenses = []

@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = request.json
    expenses.append(expense)

    if expense['amount'] > 100:
        excess_amount = expense['amount'] - 100
        notification_message = f"Exceeded budget by ${excess_amount} - Expense: ${expense['amount']} - {expense['description']}"
        notification = {'message': notification_message}
        response = requests.post('http://localhost:3002/notifications', json=notification)

    return jsonify(expense), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)
@app.route('/expense_frontend', methods=['GET'])
def expense_frontend():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3001)
