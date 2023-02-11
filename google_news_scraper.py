from pprint import pprint

from gnews import GNews

import news_persistence_client

TOPICS = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'SCIENCE', 'HEALTH']
PERIOD = '12h'
gnews_client = GNews(period=PERIOD)


def main():
    news = get_news()
    set_full_article(news)
    send_to_api(news)


def get_news():
    read = []

    for topic in TOPICS:
        read += gnews_client.get_news_by_topic(topic)

    return read


def set_full_article(news):
    for a_news in news:
        try:
            a_news['full_article'] = gnews_client.get_full_article(a_news['url']).text
        except:
            a_news['full_article'] = ''


def send_to_api(news):
    for a_news in news:
        return news_persistence_client.send_to_api(a_news)


main()
