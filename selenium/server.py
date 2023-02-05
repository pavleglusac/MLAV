from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fastapi import FastAPI
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

app = FastAPI()
ser = Service(r"./chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--user-data-dir=./tmp/tmp")
driver = webdriver.Chrome(service=ser, options=chrome_options)
driver.get("https://html5.gamedistribution.com/e77228250300451592b2ce1713c5eba1/?gdpr-targeting=1&gd_sdk_referrer_url=https%3A%2F%2Fgameforge.com%2Fen-US%2Flittlegames%2Ffree-helicopter-flying-simulator%2F%23")
#
# cookie_xpath = "//*[@id='cn-notice-buttons']/a[2]"
#
# WebDriverWait(driver, 10).until(EC.visibility_of((By.XPATH, cookie_xpath)))
# cookies = driver.find_element(By.XPATH, value=cookie_xpath)
# cookies.click()

@app.get("/")
def read_root():
    return {"Hello": "World"}

command_keys = {
    "up": Keys.UP,
    "down": Keys.DOWN,
    "forward": "w",
    "backward": "s",
    "left": "a",
    "right": "d"
}


@app.get("/execute/{command}")
def execute_commands(command):
    element = driver.find_element(by=By.XPATH, value="/html/body")
    print("Executing: " + command)
    t_end = time.time() + 10
    command_key = command_keys[command]
    while time.time() < t_end:
        # driver.execute_script('el = document.elementFromPoint(250, 250); el.click();')
        time.sleep(200)
        element.send_keys(Keys.UP)