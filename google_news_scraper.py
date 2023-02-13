import uuid
from pprint import pprint

from gnews import GNews

import news_persistence_client
from news_analyzer_client import search_companies

TOPICS = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'SCIENCE', 'HEALTH']
PERIOD = '3h'
gnews_client = GNews(period=PERIOD)


def main():
    news = get_news()
    set_full_article(news)
    get_news_companies(news)
    send_to_api(news)


def get_news():
    news = []

    for topic in TOPICS:
        news = [*news, *gnews_client.get_news_by_topic(topic)]

    return news


def set_full_article(news):
    for a_news in news:
        try:
            a_news.update({
                'full_article': gnews_client.get_full_article(a_news["url"]).text
            })
        except:
            a_news.update({
                'full_article': ''
            })


def send_to_api(news):
    for a_news in news:
        news_to_send = {
            'id': uuid.uuid1().int >> 64,
            'title': a_news['title'],
            'body': a_news['full_article'],
            'date': a_news['published date'],
            'url': a_news['url'],
            'site': {
                'url': a_news['publisher']['href'],
                'name': a_news['publisher']['title'],
            }
        }

        return news_persistence_client.send_to_api(news_to_send)


def get_news_companies(news):
    for a_news in news:
        search_companies(a_news)


main()
