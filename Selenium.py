import os 
import time
os.system('cls')




from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By 

service = Service(r"C:\Users\617924867\GIT DEMO\python-practice\msedgedriver.exe")

driver = webdriver.Edge(service=service)

driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID,"firstName").send_keys("Sudhanshu ")
driver.find_element(By.ID,"userEmail").send_keys("sudhanshu.raj@gmail.com")
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys(8002444948)



driver.find_element(By.ID,"gender-radio-2").click()
driver.find_element(By.XPATH, "//input[@Class_Name ='btn']").click()
driver.find_element(By.CSS_SELECTOR, "input[id ='currentAddress']").click()









time.sleep(5)




























































time.sleep(2)