def fetch_wikipedia_url(question):
    search_url = f"https://en.wikipedia.org/w/index.php?search={question.replace(' ', '+')}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.select('.mw-search-results')
    if search_results:
        first_result = search_results[0].select_one('a')
        if first_result:
            article_url = f"https://en.wikipedia.org{first_result.get('href')}"
            return article_url
    return None
