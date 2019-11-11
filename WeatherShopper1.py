"""Scope:
Launch the Browser
Maximize the window
Navigate to weathershopper page
Read the weather and either go to moisturizer or sunscreen
close the browser
"""
import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#maximize the window
driver.maximize_window() 

 #navigate to URL
driver.get("https://weathershopper.pythonanywhere.com/") 

# Locate the temperature by using xpath
readWeather=driver.find_element_by_xpath("//span[@id='temperature']")
print (readWeather.text)

#when we get the elements we should convert them to int(i.e Converting web element to string/int)  
#and to remove "deg cel " we should do slicing operation
temp=int(readWeather.text[:-2])

if (temp < 19):
    driver.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]").click()
    print("Buying Moisturizers")
else:
    driver.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]").click()
    print("Buying Sunscreens")

time.sleep(8)  #wait for things to load

driver.close()  #closing the browser