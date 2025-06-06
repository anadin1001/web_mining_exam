# De pe site-ul http://www.crunchbase.com/ , pentru o companie oarecare, extrageti
# locatia companiei, numărul de angajați, website-ul și totalul fondurilor primite.

import requests, bs4
from bs4 import BeautifulSoup

headers = ({

    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90',

    'From': 'nedelcu1andreea19@stud.ase.ro'

})


URL = "https://www.crunchbase.com/organization/ibm"


def main():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    location = soup.find("span", {"class": "component--field-formatter field-type-identifier-multi"})
    location_a = location.find_all("a", {"class": "accent ng-star-inserted"} )
    finalLoc =""
    for a in location_a:
        finalLoc =finalLoc + " "+a.text
    print("Location:", finalLoc)

    employees =soup.find("a", {"class": "component--field-formatter field-type-enum accent highlight-color-contrast-light ng-star-inserted"})
    print("Employees:", employees.text)
    #
    # site = pq(dom("ul.icon_and_value li:nth-child(5)")).text()
    # print("Website:", site)
    #
    # funds = pq(dom("span.field-type-money")).text()
    # print("Total funds:", funds)


if __name__ == '__main__':
    main()

