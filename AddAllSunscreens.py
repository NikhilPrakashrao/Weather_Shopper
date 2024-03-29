"""Scope:
Launch the Browser
Maximize the window
Navigate to weathershopper sunscreen page
Add all the sun screens to the cart
close the browser
"""
import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to URL
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")

# Adding all the sunscreens to the cart
sunscreens=driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
for all_sunscreen in sunscreens:
    all_sunscreen.click()

#clicking on the cart
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

#confirming that it is redirected to the checkout page
if(driver.current_url=="https://weathershopper.pythonanywhere.com/cart"):
    print("added all SunScreens Successfully added to cart")
else:
    print("Failed to add to cart.")

#wait for things to load
time.sleep(6)

#closing the browser
driver.close()