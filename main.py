# esake scraper
from boxscore_scrape import boxscore_scrape
from boxscore_dictionary import boxscore_dictionary
from find_game_urls import find_game_urls
import multiprocessing
from upload_json import upload_json

if __name__ == '__main__':
    # scraper setup
    driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'

    # paste fixture url
    website = 'https://www.esake.gr/el/action/EsakeResults?idchampionship=DC917125&idteam=&idseason=00000001&series=05'

    urls = find_game_urls(driver_path, website)

    # Choose method to run parallel
    i = 0
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=boxscore_dictionary, args=(driver_path, url, str(i)))
        p.start()
        i += 1
        processes.append(p)
    for p in processes:
        p.join()

