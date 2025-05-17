from celery import shared_task
from webscraping.script.scraping import collect_news
import os
import csv
import django

CONFIG = {
    'DJANGO_SETTINGS_MODULE': 'news.settings',
    'CSV_FILE_NAME': 'gold_commodity.csv',
    'CSV_DIR': '/app/webscraping/scripts',
}

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      CONFIG['DJANGO_SETTINGS_MODULE'])
django.setup()


@shared_task(queue='scrapy_tasks')
def collect_news_task():
    print("Running scheduled news collection...")
    collect_news()
    return "Scraping complete"
