# esake scraper

from boxscore_scrape import boxscore_scrape
from boxscore_dictionary import boxscore_dictionary

# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://www.esake.gr/el/action/EsakegameView?idgame=4180233B&mode=2'

# boxscore_scrape(driver_path, website)
boxscore_dictionary(driver_path, website)
