
from flask import Flask
from flask import request
import os
from flask import jsonify

os.chdir("..")
from src.distance_function_main import nearest_users
app = Flask(__name__)


@app.route("/nearest_users", methods=['POST'])
def nearest_users_post():
    if request.method == 'POST':
        try:
            data = request.get_json()
            try:
                user_id = float(data.get("user_id"))
            except ValueError:
                message = 'Enter a Integer Number for User ID'
                error = {'error': message}
                return jsonify(error)
            try:
                number_of_neighbours = float(data.get("number_of_neighbours"))
            except ValueError:
                message = 'Enter a Integer Number for number of Near Users to Return'
                error = {'error': message}
                return jsonify(error)
            nearest_users_id = nearest_users(user_id, number_of_neighbours)

        except ValueError:
            message = 'Enter a user_id and number of neighbours'
            error = {'error': message}
            return jsonify(error)


        x = {'Nearest_Users': nearest_users_id}
        return jsonify(x)

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)