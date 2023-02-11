import uuid

import requests

URL = "https://3zatz1zi5g.execute-api.us-east-1.amazonaws.com/api/news"


def send_to_api(news):
    news_to_send = {
        'id': uuid.uuid1().int >> 64,
        'title': news['title'],
        'body': news['full_article'],
        'date': news['published date'],
        'url': news['url'],
        'site': {
            'url': news['publisher']['href'],
            'name': news['publisher']['title'],
        }
    }

    return requests.post(URL, json=news_to_send)
