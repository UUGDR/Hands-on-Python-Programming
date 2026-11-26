# Web Scraper: books.toscrape.com
# Fill in every ________ to complete the program.
import csv
import json
import ________
import time

import requests
from bs4 import ________

BASE_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
HEADERS = {'User-Agent': 'BookScraperLearning/1.0 (student project)'}
RATINGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
MAX_PAGES = 3


def fetch_page(url):
    """Download one page and return a BeautifulSoup object, or None if it fails."""
    try:
        response = requests.________(url, headers=HEADERS, timeout=10)
        response.________()
    except requests.________ as error:
        print(f'  Could not fetch {url}: {error}')
        return None
    return BeautifulSoup(response.________, 'html.parser')


def parse_book(article):
    """Pull the four fields out of one <article class="product_pod"> and clean them."""
    title = article.h3.a[________]           # the link text is shortened; the title attribute is complete
    price_text = article.________('p', class_='price_color').text
    rating_word = article.find('p', class_='star-rating')[________][1]
    stock_text = article.find('p', class_='availability').text
    return {
        'title': title,
        'price': float(re.________(r'[^0-9.]', '', price_text)),
        'rating': RATINGS[rating_word],
        'in_stock': 'In stock' ________ stock_text,
    }


def scrape(max_pages):
    """Visit each page in turn and collect every book."""
    books = []
    for page in ________(1, max_pages + 1):
        soup = fetch_page(BASE_URL.________(page))
        if soup is None:
            break
        articles = soup.________('article.product_pod')
        print(f'Page {page}: found {len(articles)} books')
        for article in articles:
            books.________(parse_book(article))
        time.________(1)                     # be polite: pause between requests
    return books


def save_csv(books, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.________(file, fieldnames=['title', 'price', 'rating', 'in_stock'])
        writer.________()
        writer.________(books)


def save_json(books, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.________(books, file, indent=2)


# --- Main program ---
books = scrape(MAX_PAGES)
if not books:
    raise SystemExit('No books were scraped - check your internet connection.')
save_csv(books, 'books.csv')
save_json(books, 'books.json')

prices = [book['price'] for book in books]
cheapest = ________(books, key=lambda book: book['price'])
dearest = ________(books, key=lambda book: book['price'])
print()
print(f'Books collected : {len(books)}')
print(f'Average price   : £{sum(prices) / len(prices):.2f}')
print(f'Cheapest        : {cheapest["title"]} (£{cheapest["price"]:.2f})')
print(f'Most expensive  : {dearest["title"]} (£{dearest["price"]:.2f})')
print(f'In stock        : {sum(book["in_stock"] for book in books)} of {len(books)}')
print(f'Ratings valid   : {all(1 <= book["rating"] <= 5 for book in books)}')

with open('books.json', encoding='utf-8') as file:
    print(f'Saved and reloaded: {len(json.________(file))} books in books.json')
