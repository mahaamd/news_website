import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from news.models import News


def collect_news():
    urls = [
        'https://www.zoomit.ir/laptop/',
        'https://www.zoomit.ir/tablet/',
        'https://www.zoomit.ir/tv/',
        'https://www.zoomit.ir/wearables/',
        'https://www.zoomit.ir/hardware/',
        'https://www.zoomit.ir/tech-iran/',
        'https://www.zoomit.ir/software-application/',
        'https://www.zoomit.ir/os/',
        'https://www.zoomit.ir/internet-network/',
        'https://www.zoomit.ir/gaming/',
        'https://www.zoomit.ir/cryptocurrency/',
        'https://www.zoomit.ir/mobile/',
    ]

    total_added = 0

    for url in urls:
        try:
            print("check the script running")
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            contents = soup.find_all('p', class_='sc-9996cfc-0 enskxE')
            tags = soup.find_all(
                'span', class_='sc-9996cfc-0 dvzXZE sc-4c41eafb-5 lmthOZ')

            count = min(len(tags), len(contents))
            tag_name = urlparse(url).path.strip('/')

            for i in range(count):
                title = tags[i].text.strip()
                content = contents[i].text.strip()

                _, created = News.objects.get_or_create(
                    title=title,
                    defaults={
                        'content': content,
                        'tag': tag_name,
                        'source': url,
                    }
                )
                if created:
                    total_added += 1

        except Exception as e:
            print(f"Error processing {url}: {e}")

    print(f"News update completed. {total_added} new items added.")
