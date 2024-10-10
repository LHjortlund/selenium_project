from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#keep Chrome browser open after program finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Zulay-Super-Automatic-Coffee-Machine/dp/B0CSPQ5LZX/ref=sr_1_5?crid=3M3ISXC78COWQ&dib=eyJ2IjoiMSJ9.zzpwiIKJ1kKuyE4Z_Z_rOqAEqSWleELLwdyqPxm_xxPNAfmEFfJH26a5aPRwXYf9Gb1egWXAUO4mRMsnvronTX0ud41nu78Sovdm3YFe1AznQou-pLh7D_tYu2wPV8JKjdAwD2ONr0IIVTumjbXHzvv_cHCDhf-fHex63iav3Y-P7cOwR-eM6ktTLepowOotD6IIfIm0ucmQpb18-tHvsxnfXX3kFY3AVebAmSTrIO0.4vdoUYjN5LFtG9kSv2xpaglVTZz95s7RvkgZT2nLSO8&dib_tag=se&keywords=automatic%2Bcoffee%2Bmachine&psr=PDAY&qid=1728471506&refinements=p_n_feature_seven_browse-bin%3A23971110011%2Cp_72%3A1248915011%2Cp_n_condition-type%3A6358196011&rnid=6358194011&s=pbdd&sprefix=automatic%2B%2Cpbdd%2C213&sr=1-5&th=1")
time.sleep(15)

price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(price_dollars.text + "," + price_cents.text + " dollars")


# driver.close()
driver.quit()
