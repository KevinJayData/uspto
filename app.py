from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Connect webdriver to chrome
browser = webdriver.Chrome(ChromeDriverManager().install())  #executable_path='/Users/kevinjay/projects/gecko/chromedriver.exe')
browser.get('https://tsdr.uspto.gov/')

serial_input = browser.find_element(By.ID, 'searchNumber')
serial_input.send_keys('85931937' + Keys.RETURN)

values = browser.find_elements(By.CLASS_NAME, 'value')
print(values)

print('I kinda know what im doing')