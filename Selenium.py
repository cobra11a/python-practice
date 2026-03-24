import os 
import time
from selenium.webdriver.support.ui import Select
os.system('cls')




from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By 

service = Service(r"C:\Users\617924867\GIT DEMO\python-practice\msedgedriver.exe")

driver = webdriver.Edge(service=service)

driver.maximize_window()

# driver.get("https://demoqa.com/automation-practice-form")

# driver.find_element(By.ID,"firstName").send_keys("Sudhanshu ")
# driver.find_element(By.ID,"userEmail").send_keys("sudhanshu.raj@gmail.com")
# driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys(8002444948)



# driver.find_element(By.ID,"gender-radio-2").click()
# driver.find_element(By.XPATH, "//input[@Class_Name ='btn']").click()
# driver.find_element(By.CSS_SELECTOR, "input[id ='currentAddress']").click()

# driver.get("https://demoqa.com/text-box")
# time.sleep(2)
# driver.find_element(By.ID ,"userName").send_keys("Sonu")
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
# time.sleep(2)

# text = driver.find_element(By.ID ,"name").text
# time.sleep(2)

# print(text)


# driver.get("https://demoqa.com/broken")
# time.sleep(2)

# driver.find_element(By.LINK_TEXT ,"Click Here for Valid Link").click()


# **** Select class for static dropdown 

# driver.get("https://rahulshettyacademy.com/dropdownsPractise")
# dropdown = Select(driver.find_element (By.ID, "ctl00_mainContent_DropDownListCurrency")) # the whole dropdown box 

# time.sleep(2)

# dropdown.select_by_value("USD") # select USD 
# dropdown.select_by_index("2") 
# dropdown.select_by_visible_text("USD") 

# print(dropdown.first_selected_option.text) # print message of selected option 


# ****Autosuggestive drop down dynamically dropdown *****


driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element(By.ID ,"autosuggest").send_keys("Aus")
time.sleep(2)

message = driver.find_elements(By.CSS_SELECTOR , "li[class ='ui-menu-item'] a ")

print(len(message))

for suggestion in message:
    # print("Option:", suggestion.text)
    # if suggestion.text == "Australia" :
    #     suggestion.click()
    #     break
 if suggestion.text == "Australia":
        suggestion.click()
        break 








time.sleep(5)






















































