from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#challenge print the statistic number in front page
special_statistics_link = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(special_statistics_link.text)
driver.quit()