"""Scope:
Launch the Browser
Maximize the window
Navigate to weathershopper sunscreen page
Add all the sun screens to the cart
check the items in the cart
click on pay by card and fill the payment details
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

#finding the xpath for locating table:
table=driver.find_element_by_xpath("//table[@class='table table-striped']")

#counting rows in the cart table
count_rows=table.find_elements_by_xpath("//tbody/descendant::tr")
print ("There are",len(count_rows),"items in the cart")

#Finding the total amount of the cart:
total_amount=driver.find_element_by_xpath("//p[@id='total']")
print("Total amount of the items in the cart is Rupees:",total_amount.text[-4::])

driver.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

driver.find_element_by_xpath("//input[@type='email']").send_keys("kkiyghf@qxf3.com")
driver.find_element_by_xpath("//input[contains(@type,'tel')]").send_keys(4242424242424242)
driver.find_element_by_xpath("//input[contains(@placeholder,'MM / YY')]").send_keys('09/35')
driver.find_element_by_xpath("//input[contains(@placeholder,'CVC')]").send_keys('963')
driver.find_element_by_xpath("//input[contains(@placeholder,'ZIP Code')]").send_keys("585969")
driver.find_element_by_xpath("//div[contains(@class,'Checkbox-tick')]").click()
driver.find_element_by_xpath("//input[contains(@autocomplete,'mobile tel')]").send_keys('1234567890')
driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()


#wait for things to load
time.sleep(6)

#closing the browser
driver.close()