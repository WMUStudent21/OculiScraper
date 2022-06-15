# Purely desc. extractor, for public reference

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
driver.get('https://www.oculus.com/experiences/quest/1995434190525828/')

desc = driver.find_element(by=By.XPATH, value='//div[@class="clamped-description__content"]')

data = {
    'description': desc.text 
}

print(data)
driver.quit()
