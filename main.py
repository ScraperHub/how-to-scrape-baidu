from crawling import crawl
from scraping import scrape_html
import json

html = crawl("https://www.baidu.com/s?ie=utf-8&wd=苹果%20iPhone")
data = scrape_html(html)

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)
