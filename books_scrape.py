import requests
from bs4 import BeautifulSoup


#URL
url="http://books.toscrape.com/catalogue/page-1.html"

response= requests.get(url)

if response.status_code == 200:
    soup=BeautifulSoup(response.text,'html.parser')

    books=soup.find_all('article',class_='product_pod')

    # Loop through each book and print details

    for book in books:
        title = book.h3.a['title']
        
        price=book.find('p',class_='price_color').text.strip()
        # .text gives the textual content and .strip removes any leading and trailing whitespace
        availability=book.find('p',class_='instock availability').text.strip()
        rating=book.p['class'][1]
        print(f"Title :{title}\n Price:{price}\n Availability:{availability}\nRating: {rating}\n")

# book.p['class']:

# This retrieves the value of the class attribute as a list: ['star-rating', 'Three'].

# book.p['class'][1]:

# This accesses the second element in the class list, which is the actual rating (e.g., "Three").







