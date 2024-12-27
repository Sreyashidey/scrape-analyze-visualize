from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
file=0
driver = webdriver.Chrome()
for i in range(1,8):
    driver.get(f"https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?isCarouselView=false&limit=50&page={i}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
    elems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'productContainer')]"))
    )
    print(f"{len(elems)} items found")
    for elem in elems:
        d=elem.get_attribute("outerHTML")
        with open(f"data/{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file+=1
    time.sleep(2)
driver.close()