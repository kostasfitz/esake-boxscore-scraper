# esake scraper

from boxscore_scrape import boxscore_scrape


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://www.esake.gr/el/action/EsakegameView?idgame=4180233B&mode=2'

boxscore_scrape(driver_path, website)
