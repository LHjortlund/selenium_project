from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)
#navigate to the wished URL Page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#challenge print the statistic number in front page
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

#XPATH to the solution
# special_statistics_link = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(special_statistics_link.text)

#interaction with the achor link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()


#interact with search bar - type a wished text in the search bar on the front page
search_bar = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
search_bar.click()

#using search nar
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")


# driver.quit()

