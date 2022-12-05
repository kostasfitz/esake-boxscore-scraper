import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from upload_json import upload_json
import json


def boxscore_dictionary(driver_path, website, game_number):
    driver = webdriver.Chrome(driver_path)
    driver.get(website)

    t.sleep(2)
    dic = {'date': '', 'time': '', 'stadium': '', 'tv-channel': '', 'gameinfo': '',
           'refs': '',
           'home': {'name': '', 'players': ''},
           'away': {'name': '', 'players': ''}
           }

    # getting game info
    info_table = driver.find_element(by=By.XPATH, value="//table[@class='general']").get_attribute('innerText')
    date_time, general = info_table.split('|', 1)
    date, time = date_time.split('\n')
    stadium_tv, game_info = general.split('	', 1)
    stadium, tv = stadium_tv.split('/', 1)
    # finding game referees
    refs = driver.find_element(by=By.XPATH,
                               value="/html/body/center/div/div[5]/div/table/tbody/tr[2]/td/div/div/center[1]/table/tbody/tr/td[1]/div[2]").get_attribute('innerText')
    # assign game info values into dictionary
    dic['date'] = date
    dic['time'] = time
    dic['stadium'] = stadium
    dic['tv_channel'] = tv
    dic['gameinfo'] = game_info
    dic['refs'] = refs

    # home and away boxscore tables
    tables = driver.find_elements(by=By.XPATH, value="//table[@class='esakegrid']")
    table_home = tables[0]
    table_away = tables[1]

    # HOME team boxscore
    rows = table_home.find_elements(by=By.TAG_NAME, value="tr")
    home_team, *_ = rows[0].get_attribute('innerText').split('\n')
    dic['home']['name'] = home_team

    home_player_list = []
    for row in rows[2:-1]:
        elements = row.find_elements(by=By.TAG_NAME, value="td")
        stat = []
        for element in elements:
            stat.append(element.get_attribute('innerText'))
        stat_dic = {'#': stat[0], 'NAME': stat[1], 'MIN': stat[2], 'P': stat[3],
                        '2PM-A': stat[4], '3PM-A': stat[5], 'FTM-A': stat[6], 'REBS': stat[7], 'DREBS': stat[8],
                        'OREBS': stat[9],
                        'AST': stat[10], 'BLK': stat[11], 'BLKON': stat[12], 'FOULS F': stat[13], 'FOULS M': stat[14],
                        'STL': stat[15],
                        'TO': stat[16], 'RANK': stat[17]}
        home_player_list.append(stat_dic)

    dic['home']['players'] = home_player_list


    # AWAY team boxscore
    rows = table_away.find_elements(by=By.TAG_NAME, value="tr")
    away_team, *_ = rows[0].get_attribute('innerText').split('\n')
    dic['away']['name'] = away_team

    away_player_list = []
    for row in rows[2:-1]:
        elements = row.find_elements(by=By.TAG_NAME, value="td")
        stat = []
        for element in elements:
            stat.append(element.get_attribute('innerText'))
        stat_dic = {'#': stat[0], 'NAME': stat[1], 'MIN': stat[2], 'P': stat[3],
                    '2PM-A': stat[4], '3PM-A': stat[5], 'FTM-A': stat[6], 'REBS': stat[7], 'DREBS': stat[8],
                    'OREBS': stat[9],
                    'AST': stat[10], 'BLK': stat[11], 'BLKON': stat[12], 'FOULS F': stat[13], 'FOULS M': stat[14],
                    'STL': stat[15],
                    'TO': stat[16], 'RANK': stat[17]}
        away_player_list.append(stat_dic)

    dic['away']['players'] = away_player_list

    # exporting dictionary as json
    json_boxscore = json.dumps(dic, indent=4)
    json_file = open("boxscore"+game_number+".json", "w")
    json_file.write(json_boxscore)
    json_file.close()

    #upload_json(game_number)
