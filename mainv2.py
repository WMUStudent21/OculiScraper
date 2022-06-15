from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# URL to scrape from.
url = 'https://www.oculus.com/experiences/quest/section/1888816384764129'


# Opens a window to extract description hidden in [event] after preloading
def extract(uri):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(40) # gives an implicit wait for 40 seconds
    driver.get(uri)

    desc = driver.find_element(by=By.XPATH, value='//div[@class="clamped-description__content"]').text

    driver.quit()
    return desc

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# Runs Chrome as an automated browser (can be commanded)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(60) # gives an implicit wait for 60 seconds
driver.get(url)
body = driver.find_element_by_xpath('/html/body')

# (command) Scrolls x times to preload page //primitive
x = 950
for i in range(x):
    body.send_keys(Keys.PAGE_DOWN)

# Reads whitelist of Oculus titles
with open('whitelist_oculus.txt') as f:
    game_search = f.read().splitlines() 
f.close()

# Writes to output.txt in a single pass
with open("output.txt", "w") as f:
    f.write("{\n\n")
    for title in game_search:
        # Validates title typo/missing on user-end via notified output
        try:   
            # Fetches the 'href' URI of a game title
            link = driver.find_element(by=By.XPATH, value="//div[@class='store-section-item__meta-name' and contains(text(), '" + title + "')]/ancestor::div[@class='store-section-item']/a[@class='store-section-item-tile']").get_attribute("href")
            desc = extract(link)
        except:
            desc = 'No description'
        f.write("'{}'\n===========================\n'{}'\n\n".format(title, desc))
    f.write("}")

f.close()
driver.quit()