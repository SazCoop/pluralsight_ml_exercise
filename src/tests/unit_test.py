
##IN PROGRESS



import unittest
from flask import Flask
import requests
from flask import jsonify


class TestFlaskApiUsingRequests(unittest.TestCase):
    def nearest_users_post(self):
        response = requests.post('http://localhost:80/nearest_users', json={"user_id": "7" , "number_of_neighbours": "5"}
        self.assertEqual(response.json(), {"Nearest_Users": " 5440 3353 1499 3698 7801 "})