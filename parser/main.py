import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

from bs4 import BeautifulSoup

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#
#
# driver.get("https://qe.com.qa/en/companymoreinformationsearch?CompanyCode=QNBK")
# time.sleep(10)
# print(driver.page_source)


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome()
driver.get("https://qe.com.qa/en/companymoreinformationsearch?CompanyCode=CBQK")
time.sleep(5)
innerHTML = driver.execute_script("return document.documentElement.outerHTML")
time.sleep(5)


soup = BeautifulSoup(innerHTML, 'html.parser')
news = soup.find_all("div", class_="col-12 pl-0")
print(len(news))

for i in news:
    print(i.find("p", class_="small-text"))
    print()



# details = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Details')
# print(details)
# print(len(details))

