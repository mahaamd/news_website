from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.zoomit.ir/mobile/')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# Get all <p> tags
paragraphs = soup.find_all('p')

# Print all <p> content
for p in paragraphs:
    text = p.get_text(strip=True)
    if text:
        print(text)
        print('—' * 40)

print('—' * 100)

# Get all <span> tags inside <a> tags
span_in_a = soup.select('a span')

# Print the <span> contents
for span in span_in_a:
    text = span.get_text(strip=True)
    if text:
        print(text)
        print('—' * 40)
