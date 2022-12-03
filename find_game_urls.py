from selenium import webdriver
from selenium.webdriver.common.by import By


def find_game_urls(driver_path, website):
    driver = webdriver.Chrome(driver_path)
    driver.get(website)

    urls = set()
    containers = driver.find_elements(by=By.XPATH, value="//a[@title='Στατιστικά']")
    for container in containers:
        urls.add(container.get_attribute('href'))

    return urls
