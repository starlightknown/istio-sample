from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

BUDGETING_FRONTEND_ALIAS = 'budgeting-frontend'  # Alias of Budgeting Frontend in docker-compose
BUDGETING_FRONTEND_PORT = 5051  # Port exposed by Budgeting Frontend in docker-compose

app.secret_key = 'thisisjustarandomstring'

expenses = []
categories = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        expenses.append({'description': description, 'amount': amount, 'category': category})
    return render_template('index.html', expenses=expenses, categories=categories)

@app.route('/add_category', methods=['POST'])
def add_category():
    category_name = request.form['category_name']
    categories.append(category_name)
    return redirect(url_for('index'))

@app.route('/goto_budgeting', methods=['GET'])
def goto_budgeting():
    budgeting_frontend_url = "http://budgeting-frontend:5051"
    return redirect(budgeting_frontend_url)

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")

