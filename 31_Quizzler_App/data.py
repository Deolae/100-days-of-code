import requests

response = requests.get(url="https://opentdb.com/api.php?amount=15&type=boolean")
question_data = response.json()["results"]
