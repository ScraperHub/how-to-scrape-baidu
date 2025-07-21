from bs4 import BeautifulSoup

def scrape_html(html: str) -> dict:
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.title.string if soup.title else None
    search_input = soup.find('input', {'name': 'wd'})
    search_query = None
    if search_input:
        search_query = search_input.get('value', '')

    search_results = []
    for result in soup.select('div.title-box_4YBsj h3.t'):
        title = result.text
        url = result.find('a')['href']
        search_results.append({
            'title': title,
            'url': url
        })
    
    related_searches = []
    for result in soup.select('table.rs-table_3RiQc tr td a'):
        title = result.text
        url = result['href']
        related_searches.append({
            'title': title,
            'url': url
        })

    page_data = {
        'title' : title,
        'searchQuery': search_query,
        'searchResults': search_results,
        'relatedSearches': related_searches
    }
    
    return page_data
