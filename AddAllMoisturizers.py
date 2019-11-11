"""Scope:
Launch the Browser
Maximize the window
Navigate to weathershopper Moisturizer page
Add all the Moisturizers to the cart
close the browser
"""
import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to URL
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

# Adding all the moisturizers to the cart
moisturizers=driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
for all_Moisturizers in moisturizers:
    all_Moisturizers.click()
print("Added all Moisturizers to cart")

#wait for things to load
time.sleep(6)

#closing the browser
driver.close()