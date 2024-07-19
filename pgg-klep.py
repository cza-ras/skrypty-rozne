#otwieranie strony sklepu PGG i dodawanie wybranego artykułu do koszyka

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Safari()
driver.get("https://sklep.pgg.pl")


atrybut="//*[@id='main']/div/div[3]/div[6]/form/button"
l =driver.find_element(by=By.XPATH, value=atrybut)
#l.click()

print(driver.title)
