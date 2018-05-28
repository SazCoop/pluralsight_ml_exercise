
from flask import Flask
import os 

os.chdir("../pluralsight_ml_exercise")
from src.distance_function_main import nearest_users
app = Flask(__name__)


@app.route("/nearest_users", methods=['POST'])
def nearest_users_post():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user_id = float("user_id")
            user_id = float("number_of_neighbours")
            nearest_users =  nearest_users(user_id, number_of_neighbours)
        except ValueError:
            return jsonify("""Please enter a {"user_id": X}, {"number_of_neighbours": X}""")

        return jsonify(nearest_users)

if __name__ == '__main__':
    app.run(host='localhost', port=80)