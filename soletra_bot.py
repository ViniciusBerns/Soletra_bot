import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time





def extract_words(data):
    words = [item['word'] for item in data.get('word_list', []) if 'word' in item]
    return words

with open('soletra.json','r') as file:
    json_string = json.load(file)


words = extract_words(json_string)
# print(words)



driver = webdriver.Chrome()
driver.get("https://g1.globo.com/jogos/soletra/")
assert "Soletra" in driver.title
time.sleep(3)



inicio = driver.find_element(By.CLASS_NAME, 'intro-button')
inicio.send_keys(Keys.ENTER)
time.sleep(3)


inicio = driver.find_element(By.CLASS_NAME, 'drawer-close-icon')
inicio.send_keys(Keys.ENTER)
time.sleep(2)

resp = driver.find_element(By.ID, 'input')



for item in words:
    # resp.click()
    resp.send_keys(item)
    time.sleep(0.5)
    resp.send_keys(Keys.ENTER)
    # resp.clear()
    time.sleep(0.5)


driver.quit()