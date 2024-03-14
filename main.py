from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# driver is such a bridge
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element("id", value="cookie")


while True:
    money = driver.find_element("id", value="money")

    if money: 
        continue

    cookie.click()

# print(amount.text.split()[0])

# english = driver.find_element("link text", "English")
# english.click()

# search = driver.find_element("name", "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

