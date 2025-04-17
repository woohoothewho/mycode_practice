import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://orteil.dashnet.org/cookieclicker/")

consent_id = '[aria-label="Consent"]'
language_id = 'langSelect-EN'
main_cookie_id = 'bigCookie'
cookie_count_id = 'cookies'
product_price_id = 'productPrice'
product_prefix = 'product'

#Agree to personal data
consent = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, consent_id)))
consent.click()

#Select language
language = wait.until(EC.visibility_of_element_located((By.ID, language_id)))
language.click()

# time.sleep(100)

#Click Cookie
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.ID, main_cookie_id)))
cookie = driver.find_element(By.ID, main_cookie_id)

for _ in range(16):
    cookie.click()
time.sleep(5)

wait.until(EC.element_to_be_clickable((By.ID, 'product0')))

product = driver.find_element(By.ID, 'product0')
product.click()

for _ in range(100):
    cookie.click()

wait.until(EC.element_to_be_clickable((By.ID, 'upgrade0')))

upgrade = driver.find_element(By.ID, 'upgrade0')
upgrade.click()

for _ in range(250):
    cookie.click()

upgrade = driver.find_element(By.ID, 'upgrade0')
upgrade.click()


for _ in range(10000):
    cookie.click()
    
    cookies_count = driver.find_element(By.ID, cookie_count_id).text.split(" ")[0]
    cookies_count = int(cookies_count)

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_id+str(i)).text.replace(",", "")
        if cookies_count >= int(product_price):
            product = driver.find_element(By.ID, product_prefix+str(i))
            product.click()
        else:
            continue





time.sleep(100)

driver.quit()