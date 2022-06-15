from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def extract(uri):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(40) # gives an implicit wait for 20 seconds
    driver.get(uri)

    desc = driver.find_element(by=By.XPATH, value='//div[@class="clamped-description__content"]').text

    driver.quit()
    return desc

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
url = 'https://www.oculus.com/experiences/quest/section/1888816384764129'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() # For maximizing window
driver.implicitly_wait(30) # gives an implicit wait for 20 seconds
driver.get(url)

with open('whitelist_oculus.txt') as f:
    game_search = f.read().splitlines() 
f.close()

data = {}

# with open('output.txt', 'w') as f:
for title in game_search:    
    link = driver.find_element(by=By.XPATH, value="//div[@class='store-section-item__meta-name' and contains(text(), '" + title + "')]/ancestor::div[@class='store-section-item']/a[@class='store-section-item-tile']").get_attribute("href")
    desc = extract(link)
    curr = {    title : desc    }
    data.update(curr)
    # print(curr, file=f)

f = open("output.txt", "w")
f.write("{\n")
for k in data.keys():
    f.write("'{}'\n===========================\n'{}'\n\n".format(k, data[k]))
f.write("}")

f.close()
driver.quit()