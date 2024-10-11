from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

#interact with FIRST NAME bar
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Holly", Keys.ENTER)

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Molly", Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("HollyMolly@gmail.com", Keys.ENTER)

#locate the "sign in" button
submit = driver.find_element(By.CSS_SELECTOR,"btn")
submit.click()