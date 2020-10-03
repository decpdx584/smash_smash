import datetime, re, requests, io, time, random, string
from bs4 import BeautifulSoup
from models import app, db, Fighter_one, Fighter_two
from crud.fighter_crud import create_fighter
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

page = requests.get('https://www.ssbwiki.com/Fighter')
soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all("table")
fighter_table = tables[2]
tab_data = [[cell.text for cell in row.find_all(["th","td"])]
            for row in fighter_table.find_all("tr")]

fighter_list = tab_data[1:-3]

names = []
for i in range(len(fighter_list)):
    fighter = fighter_list[i]
    fighter_name = fighter[0].replace('\n', '')
    names.append(fighter_name)
names.remove('Charizard')
names.remove('Ivysaur[5]')
names.remove('Squirtle[5]')
final_names = []
for i in range(len(names)):
    name = names[i]
    if name == 'Steve[13]':
        final_names.append(name[:-4])
    elif name[-1] == ']':
        final_names.append(name[:-3])
    else:
        final_names.append(name)

    wiki_url = f'https://www.ssbwiki.com/{final_names[i]}_(SSBU)'
    r = requests.get(wiki_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    uni = soup.select('a[title*="\(universe\)"]')
    final_uni = uni[0].getText()
    avail = soup.select('table .infobox')
    info = avail[-1].text.replace('\n', ' ').split('  ')
    availability = info[-4]
    final_smash = info[-2]
    quo = soup.select('table #text')
    quote = quo[-1].text
    
    create_fighter (
        name = f'{final_names[i]}',
        universe = final_uni,
        availability = availability,
        final_smash = final_smash,
        quote = quote,
        wiki_url = wiki_url
    )

    time.sleep(2)