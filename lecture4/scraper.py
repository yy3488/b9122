import bs4
import requests
import subprocess


# TODO: change these values to suit your case.
URL = "https://www.ebay.com/itm/395704379225"
MAX_PRICE = 20
PRICE_START = "US $"


def get_html(url=URL):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    html = requests.get(url, headers=headers).text

    return html
    

def get_price(url=URL):
    html = get_html(url)

    soup = bs4.BeautifulSoup(html, features="html.parser")

    # TODO: change the rest of this function to suit your 
    
    # Select the right div. Notice the # for an ID.
    results = soup.select("div#RightSummaryPanel")

    # The result is a vector, so choose the first one.
    price_div = results[0]

    # Select the right price. Note the . for a class.
    results = price_div.select("div.x-price-primary")

    # Again, a vector, so choose the first one.
    price_tag = results[0]

    # Convert the price tag to text.
    price = price_tag.get_text()
    assert price.startswith(PRICE_START)

    price = float(price.replace(PRICE_START, ""))
    print("Price is " + str(price))
    return price


if "__main__" == __name__:
    price = get_price(URL)
    if price < MAX_PRICE:
        subprocess.check_output("open " + URL, shell=True)
