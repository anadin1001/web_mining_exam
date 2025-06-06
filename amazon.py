# Subiectul 1
#
# De pe 10 pagini de amazon.com a unor cărți extrageți titlul cărții, autorul și anul de publicare.

import requests, bs4
from bs4 import BeautifulSoup

headers = ({

    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90',

    'From': 'nedelcu1andreea19@stud.ase.ro'

})

urls = ['https://www.amazon.com/gp/product/B08H17FP36/ref=s9_acss_bw_cg_BOTM_3a1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=ZJ5X1SYG0FVZFVSYBPZS&pf_rd_t=101&pf_rd_p=5303074b-649d-470b-b459-8c27e11282c9&pf_rd_i=17143709011']


for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup_books = soup.find("span", {"id": "productTitle"})  # books
    spanAuthor=soup.find("span", {"class": "author notFaded"})
    soup_authors = spanAuthor.find("a", {"class": "a-link-normal"})  # authors
    div_an = soup.find('div', {"class": "a-section a-spacing-small a-padding-small"})
    a_an= div_an.find('span', {'class': "a-text-bold"})

    print("Titlu: " + soup_books.text)
    print("Autor: " + soup_authors.text)
    print("An: " + a_an.text[-5:-1])