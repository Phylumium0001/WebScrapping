from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://fitgirl-repacks.site/page/2/?ref=cybrhome')    # Obtain info from the site

soup = BeautifulSoup(html_text.text, 'lxml')        # Creates an instant of Bs
container = soup.find_all('article')                # Searches for article tags

#  Titles
for tag in container:                               
    anchor = tag.h1.a.text          # Title

    div = tag.find('div', class_='entry-content')   # Sizes
    pTags = div.find('p')
    strongTags = pTags.find_all('strong')                  

    link = tag.header.h1.a['href']

    if anchor == 'Upcoming Repacks':
        continue
    else:
        print(f'Title : {anchor}')
        print(f'Original Size : {strongTags[-2].text}')
        print(f'Repack Size : {strongTags[-1].text}')
        print(f'Link : {link}')
        print('')

