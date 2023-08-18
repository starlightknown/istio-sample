from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

notifications = []

@app.route('/notifications', methods=['POST'])
def create_notification():
    notification = request.json
    notifications.append(notification)
    return jsonify(notification), 201

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)

@app.route('/notification_frontend', methods=['GET'])
def notification_frontend():
    return render_template('notification.html')

if __name__ == '__main__':
    app.run(port=3002)
