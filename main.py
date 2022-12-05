# esake scraper

from boxscore_scrape import boxscore_scrape
from boxscore_dictionary import boxscore_dictionary
from find_game_urls import find_game_urls
from upload_json import upload_json

# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'

# paste fixture url
website = 'https://www.esake.gr/el/action/EsakeResults?idchampionship=DC917125&idteam=&idseason=00000001&series=02'

urls = find_game_urls(driver_path, website)

# Choose method
# boxscore_scrape(driver_path, website)
i = 0
for url in urls:
    boxscore_dictionary(driver_path, url, str(i))
    upload_json(str(i))
    i += 1
