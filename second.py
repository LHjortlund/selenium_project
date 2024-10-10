from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
#
# button = driver.find_element(By.ID, "submit")
# print(button.size)
#
# #find the anchor-tag to the documentation widget on python org website
# documentation_link =driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

#if everything fails then there exist XPATH
#undersøg > kopier > XPATH + husk at ændre gåseøjne, da det eksisterer inde i det vi har kopieret
# submit_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_link.text)

#Challenge: extract upcoming event data from python.org. There are 5. store them in nested
# python dictionary. print dic to the console. The event data should be stores under keys
#"time" and "name"
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in event_times:
#     print(time.text)

#find names of the events
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)
driver.quit()