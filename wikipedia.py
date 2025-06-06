# De pe pagina de wikipedia a unei monede naționale extrageți utilizatorii monedei,
# simbolul, subdiviziunile și valoarea inflației

import requests, bs4
from bs4 import BeautifulSoup

headers = ({

    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90',

    'From': 'nedelcu1andreea19@stud.ase.ro'

})


url ='https://en.wikipedia.org/wiki/Euro'


def main():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    utilizatorii_div = soup.find("div", {"class": "div-col"}).find_all("a")
        #pq(dom("div.div-col > ul > li > span.datasortkey > a"))('a').text())
    utilizatorii = ''
    for a in utilizatorii_div:
        utilizatorii = utilizatorii + ' '+a.text
    print(utilizatorii)

if __name__ == '__main__':
    main()