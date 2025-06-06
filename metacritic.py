# . De pe pagina de metacritic a unui film, extrageti regizorul, scorul mediu acordat de
# critici, scorul mediu acordat de utilizatori și durata filmului

import requests, bs4
from bs4 import BeautifulSoup

headers = ({

    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90',

    'From': 'nedelcu1andreea19@stud.ase.ro'

})

url = "https://www.metacritic.com/movie/bad-boys-ride-or-die/"

def main():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
   # details_div = (soup.find_all("div", {"class": "c-movieDetails_sectionContainer g-outer-spacing-top-small g-inner-spacing-medium u-flexbox u-flexbox-row"}))

    # details_section = soup.find_all("div", {"class": "c-movieDetails_sectionContainer g-outer-spacing-top-small g-inner-spacing-medium u-flexbox u-flexbox-row"})
    # print(details_section)
    # if details_section:
    #     # Find all span elements within this section
    #     spans = details_section.find_all('span', class_='g-outer-spacing-left-medium-fluid')
    #     if len(spans) > 1:
    #         runtime = spans[1].get_text(strip=True)
    #         return runtime
    #     else:
    #         return "Runtime span not found"
    # else:
    #     return "Details section not found"
    spans=soup.find_all("span", {"class": "g-outer-spacing-left-medium-fluid"})
    print(spans[2].text)

    p = soup.find_all("p", {"class": "g-text-xxsmall"})
    #print(p)
    directedby =''
    for a in p[0]:
        directedby = directedby + a.text
    print("-----")
    print(directedby)
if __name__ == '__main__':
    main()