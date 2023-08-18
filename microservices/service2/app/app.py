from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BUDGETING_FRONTEND_URL = 'http://budgeting-frontend:5051'  # URL of Budgeting Service

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        budget = float(request.form['budget'])
        data = {'category': category, 'budget': budget}
        response = requests.post(f'{BUDGETING_FRONTEND_URL}/set_budget', json=data)
        message = response.json()['message']
        if message == 'Budget set successfully!':
            return jsonify({'message': 'Budget set successfully!'})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5051, host="0.0.0.0")
