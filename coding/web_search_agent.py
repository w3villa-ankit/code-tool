# filename: web_search_agent.py
import requests
from bs4 import BeautifulSoup

def web_search_agent(query):
    url = "https://www.google.com/search?q=" + query

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    search_results = []
    for g in soup.find_all('div', class_='g'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            search_results.append(item)
    return search_results

# Test the agent with a query for today's weather
results = web_search_agent("today's weather")
for result in results:
    print(result['title'], result['link'])