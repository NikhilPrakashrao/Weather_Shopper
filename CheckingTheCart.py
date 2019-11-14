"""
Add all moisturizers to the cart
check how many items are in the cart and find the total amount of the cart
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

#clicking on the cart
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

#confirming that it is redirected to the checkout page
if(driver.current_url=="https://weathershopper.pythonanywhere.com/cart"):
    print("added all Moisturizers Successfully added to cart")
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

#wait for things to load
time.sleep(3)

#closing the browser
driver.close()