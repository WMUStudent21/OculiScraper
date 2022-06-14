from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
url = 'https://www.oculus.com/experiences/quest/section/1888816384764129'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() # For maximizing window
driver.implicitly_wait(50) # gives an implicit wait for 20 seconds
driver.get(url)

game_search = 'Wings 1941'
join_url = 'https://www.oculus.com'

# all_names = driver.find_elements(by=By.XPATH, value='//div[@class="store-section-item__meta-name"]')
# all_names = driver.find_elements(by=By.XPATH, value="//div[contains(text(), '" + game_search + "')]")

# for elem in all_names:
# submit = driver.find_element(by=By.XPATH, value="//div[contains(text(), '" + game_search + "')]/ancestor::a[@class='store-section-item-tile']")
submit = driver.find_element(by=By.XPATH, value="//a[@class='store-section-item-tile']/following-sibling::div[contains(text(), '" + game_search + "')]")
    # sleep(1)
print(submit.get_attribute("href"))

       



driver.quit()