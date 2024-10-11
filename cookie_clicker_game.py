from selenium import webdriver
from selenium.webdriver.common.by import By
# This class helps to check for some conditions to happen
from selenium.webdriver.support import expected_conditions as EC
# This class helps to keep waiting until an element found
from selenium.webdriver.support.ui import WebDriverWait
import time

# Number of cookies user wants to get
amount_of_cookie_to_earn = 1000

# To timeout after 5 minutes
five_minute = time.time() + 60 * 5

#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#initiate Chrome site
driver.get("https://orteil.dashnet.org/cookieclicker/")

#maximize the window size
driver.maximize_window()

#wait for the below amount (sec) to let the page load
page_delay = 20

# Wait for the cookie consent banner's "Got it!" button to become clickable
got_it_button = WebDriverWait(driver, page_delay).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all"))
)

# Click on the "Got it!" button to dismiss the cookie consent banner
got_it_button.click()

# Wait for the "Consent" button to be clickable, and then click it.
consent_button = WebDriverWait(driver, page_delay).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'fc-cta-consent')][contains(., 'Consent')]"))
)
consent_button.click()

#select language to start the game, the page takes time to load and we need to wait for the element to appear
element_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".langSelectButton.title#langSelect-EN"))
WebDriverWait(driver, page_delay).until(element_present)

#find the right language element and click
lang_select = driver.find_element(By.CLASS_NAME, value="langSelectButton.title#langSelect-EN")
lang_select.click()

#wait until the needed object is available and now start clicking after a few seconds wait
element_present = EC.presence_of_element_located((By.ID,"bigCookie"))
WebDriverWait(driver, page_delay).until(element_present)
cookie_button = driver.find_element(By.ID,"bigCookie")

#run the look for 5 minutes
while True:
    #get n amount of cookies
    for i in range(amount_of_cookie_to_earn):
        cookie_button.click()

    #Get the earned cookies count
    cookie_count = int(driver.find_element(By.CSS_SELECTOR, value="#cookies.title").text.split(" ")[0].replace(",", ""))

    #wait until the needed object is available and get the price of unlocked products
    #otherwise it might fail with no Element found
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".product.unlocked.enabled .price"))

    WebDriverWait(driver, page_delay).until(element_present)
    # We need to look for unlocked products which means they are available to buy/click
    unlocked_products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled .price")

    #Get the products prices into a list
    product_price_list = []
    for unlocked_product in unlocked_products:
        product_price_list.append(unlocked_product.text)

    #The most expensive means the last product from the store
    #get the product element which we need to click, its the last price in the list
    product_to_click = f"product{product_price_list.index(product_price_list[-1])}"

    #wait until the needed object is available and then Click on a product
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, f".product.unlocked.enabled#{product_to_click}"))

    WebDriverWait(driver, page_delay).until(element_present)

    #find the product you wish to buy/click
    unlocked_product = driver.find_element(By.XPATH, value=f'//*[@id="{product_to_click}"]')

    # Solves an issue: object is not clickable because it's down somewhere,
    # need to scroll up and make it visible for the selenium cursor
    driver.execute_script("arguments[0].scrollIntoView(true);", unlocked_product);
    # Click on a product
    unlocked_product.click()

    # After five minutes stop the loop
    if time.time() > five_minute:
        break

# #get cookie to click on
# cookie = driver.find_element(By.ID, "bigCookie")
#
# #get upgrade items ids
# items = driver.find_element(By.CSS_SELECTOR, value="#storeBulkBuy")