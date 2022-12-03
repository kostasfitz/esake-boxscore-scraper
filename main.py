# esake scraper

from boxscore_scrape import boxscore_scrape
from boxscore_dictionary import boxscore_dictionary

# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
# paste url of game boxscore
website1 = 'https://www.esake.gr/el/action/EsakegameView?idgame=F6358669&mode=2'
website2 = 'https://www.esake.gr/el/action/EsakegameView?idgame=3B7D9406&mode=2'
website3 = 'https://www.esake.gr/el/action/EsakegameView?idgame=F531AE99&mode=2'
website4 = 'https://www.esake.gr/el/action/EsakegameView?idgame=41505DAC&mode=2'
website5 = 'https://www.esake.gr/el/action/EsakegameView?idgame=B63D2BDC&mode=2'
website6 = 'https://www.esake.gr/el/action/EsakegameView?idgame=1ED90EBF&mode=2'
# Choose method
# boxscore_scrape(driver_path, website)
boxscore_dictionary(driver_path, website1, "1")
boxscore_dictionary(driver_path, website2, '2')
boxscore_dictionary(driver_path, website3, '3')
boxscore_dictionary(driver_path, website4, '4')
boxscore_dictionary(driver_path, website5, '5')
boxscore_dictionary(driver_path, website6, '6')