from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RollerCoaster:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_audible(self):
        self.driver.get("https://www.audible.in/")
        time.sleep(4)

    def search_category(self):
        browse = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[4]/div/div/div/header/div[2]/div[1]/nav/span/ul/li[2]/div/div[1]/a/span")
        browse.click()
        time.sleep(3)

        category = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[4]/div/div/div/header/div[2]/div[1]/nav/span/ul/li[2]/div/div[2]/div/div/div/div/div/div[2]/span/ul/li[4]/a")
        category.click()
        time.sleep(4)

        view_all = self.driver.find_element(By.CSS_SELECTOR, value=".bc-row a")
        view_all.click()
        time.sleep(4)

        book_title = self.driver.find_elements(By.CSS_SELECTOR,
                                               value=".bc-list-item h3 a")

        book_rating = self.driver.find_elements(By.CSS_SELECTOR, value=".ratingsLabel .bc-color-secondary")
        time.sleep(3)
        books = {}
        for n in range(len(book_title)):
            books[n] = {
                "title": book_title[n].text,
                "rating": book_rating[n].text
            }


bot = RollerCoaster()
bot.open_audible()
bot.search_category()

