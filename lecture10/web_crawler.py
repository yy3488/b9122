import doctest
import sys
import urllib.request


import bs4


#sys.setrecursionlimit(1500)


SEED_URL = "https://openclimatecurriculum.org/"

USER_AGENT_KEY = "User-Agent"
USER_AGENT_VALUE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0'

MAX_URLS = 200

def get_webpage(url):
    req = urllib.request.Request(url)
    req.add_header(USER_AGENT_KEY, USER_AGENT_VALUE)

    try:
        html = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        print("  Skipping URL that gives an error: " + url)
        return

    return html


def clean_and_join_url(url, href):
    """
    >>> clean_and_join_url("http://example.com", "/new_page#someId")
    'http://example.com/new_page'
    >>> clean_and_join_url("http://example.com", "/new_page?someParam=something")
    'http://example.com/new_page'
    """

    for marker in ["#", "?"]:
        trim_index = href.find(marker)
        if -1 != trim_index:
            href = href[:trim_index]

    return urllib.parse.urljoin(url, href)


def should_visit_url(url):

    if not url.startswith(SEED_URL):
        return False

    if url.endswith(".pdf") or "mudar" in url:
        return False

    return len(url) < 50
    

def get_links(url):

    html = get_webpage(url)
    if not html:
        return []

    soup = bs4.BeautifulSoup(html, "html.parser")

    all_urls = []
    for tag in soup.find_all("a"):
        href = tag.get("href")
        
        if not href:
            continue

        new_url = clean_and_join_url(url, href)
        all_urls.append(new_url)

    return list(set(all_urls))


def crawl(seed_url=SEED_URL):

    to_visit = [seed_url]
    visited = []
    
    while len(to_visit) > 0:

        if MAX_URLS < len(visited):
            print("  Reached maximum of %d URLs visited, exiting" % MAX_URLS)
            return

        url = to_visit.pop()
        
        if url in visited:
            print("  Skipping visited link: " + url)
            continue

        if not should_visit_url(url):
            print("  Skipping link outside of policies: " + url)
            continue
        
        print("Visited: %d, to visit: %d, visiting: %s" %
              (len(visited), len(to_visit), url))

        new_links = get_links(url)
        visited.append(url)
        for link in new_links:
            if link not in to_visit:
                to_visit.append(link)


def main():
    return crawl()


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
    main()