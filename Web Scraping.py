import requests
from bs4 import BeautifulSoup

def count_books_from_library_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    book_titles = soup.find_all('h2', class_='book-title')
    return len(book_titles)

# Example usage:
library_url = 'https://examplelibrary.com/books'
total_books = count_books_from_library_website(library_url)
print("Total books from library website:", total_books)
