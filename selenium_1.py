from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver_path = 'C:\\Users\\piyush.kaushal\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'


service = Service(driver_path)
driver = webdriver.Chrome(service=service)


url = 'https://www.nseindia.com/market-data/equity-derivatives-watch'
driver.get(url)


time.sleep(5)  


try:
   
    download_button = driver.find_element(By.XPATH, '//*[@id="dwldcsv"]')
    download_button.click()
    print("Download button clicked successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(10)
driver.quit()
