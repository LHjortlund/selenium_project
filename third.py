from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
#navigate to the wished URL Page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#challenge print the statistic number in front page
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

#XPATH to the solution
# special_statistics_link = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(special_statistics_link.text)

#interaction with the achor link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Wait until the search bar is clickable
# try:
#     search_bar = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "#p-search a"))
#     )
#     search_bar.click()
#
#     # Now interact with the search field
#     search = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "search"))
#     )
#     search.send_keys("Python", Keys.ENTER)
# except TimeoutException:
#     print("Element was not interactable within the given time")
# finally:
#
#     driver.quit()
# interact with search bar - type a wished text in the search bar on the front page
search_bar = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
search_bar.click()

# using search nar
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()