'''
This is alert sample for selenium python
Name: Arun Mannepula
'''
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///C:/Users/ARUNM/Desktop/Alert1.html")
driver.maximize_window()
# This is simple alert popup
elem1 = driver.find_element_by_xpath("//*[@id='content']/p[4]/button")
elem1.click()
alt_elem1 = Alert(driver)
assert "A simple Alert" in alt_elem1.text
alt_elem1.accept()


# This alert discmiss ction
elem2 = driver.find_element_by_xpath("//*[@id='content']/p[8]/button")
elem2.click()
alt_elem2=Alert(driver)
assert "Confirm pop up with OK and Cancel button" in alt_elem2.text
alt_elem2.dismiss()


elem3 = driver.find_element_by_xpath("//*[@id='content']/p[11]/button")
elem3.click()

alt_elem3=Alert(driver)
# print(alt_elem3.text)
assert "Do you like toolsqa?" in alt_elem3.text
sleep(4)
alt_elem3.dismiss()


driver.quit()

# assert "Google" in driver.page_source
# print("Assert pass")
# driver.close()

