from datetime import datetime
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json


def boxscore_scrape(driver_path, website):
    driver = webdriver.Chrome(driver_path)
    driver.get(website)

    t.sleep(2)
    tables = driver.find_elements(by=By.XPATH, value="//table[@class='esakegrid']")
    table_home = tables[0]
    table_away = tables[1]
    # print(table_home.get_attribute('innerText'))
    # print(table_away.get_attribute('innerText'))

    # stats for HOME team
    df_home = pd.DataFrame(columns=['#', 'NAME', 'MIN', 'P', '2PM-A', '3PM-A', 'FTM-A', 'REBS', 'DREBS', 'OREBS', 'AST',
                                    'BLK', 'BLK ON', 'FOULS F', 'FOULS M', 'STL', 'TO', 'RANK'])

    rows = table_home.find_elements(by=By.TAG_NAME, value="tr")
    for row in rows[2:-1]:
        stats = row.find_elements(by=By.TAG_NAME, value="td")
        data = []
        for stat in stats:
            data.append(stat.get_attribute('innerText'))
        print(data)
        df_home.loc[len(df_home)] = data
    print(df_home)

    # stats for AWAY team
    df_away = pd.DataFrame(columns=['#', 'NAME', 'MIN', 'P', '2PM-A', '3PM-A', 'FTM-A', 'REBS', 'DREBS', 'OREBS', 'AST',
                                    'BLK', 'BLK ON', 'FOULS F', 'FOULS M', 'STL', 'TO', 'RANK'])
    rows = table_away.find_elements(by=By.TAG_NAME, value="tr")
    for row in rows[2:-1]:
        stats = row.find_elements(by=By.TAG_NAME, value="td")
        data = []
        for stat in stats:
            data.append(stat.get_attribute('innerText'))
        print(data)
        df_away.loc[len(df_away)] = data
    print(df_away)

    df_home.to_json(r'C:\Python\esake-scraper\export_df.json', orient='index')
    driver.close()

