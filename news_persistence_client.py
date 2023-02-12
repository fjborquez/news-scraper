import requests

URL = "https://3zatz1zi5g.execute-api.us-east-1.amazonaws.com/api/news"


def send_to_api(news):
    return requests.post(URL, json=news)

