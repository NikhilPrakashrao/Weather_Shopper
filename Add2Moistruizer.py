"""Scope:

Add two moisturizers to your cart. 
First, select the least expensive mositurizer that contains Aloe. 
For your second moisturizer,  select the least expensive moisturizer that contains almond.
Click on cart when you are done."""

import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to URL
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

# Finding price of sunscreen by xpath
price_of_moisturizer=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")

new_list_to_add_Sliced_elements=[]

for index,value in enumerate(price_of_moisturizer):
    print("The index is",index,"The value is",value.text)
    

for value in price_of_moisturizer:
    print(value.text[-3::])
    new_list_to_add_Sliced_elements.append(value.text[-3::])
print(new_list_to_add_Sliced_elements)

   
# Finding names of sunscreen by xpath
names_of_moisturizer=driver.find_elements_by_xpath("//p[@class='font-weight-bold top-space-10']")

new_list_to_add_Names=[]
for index,value in enumerate(names_of_moisturizer):
    print("The index is",index,"The value is",value.text)
    new_list_to_add_Names.append(value.text)
print(new_list_to_add_Names)

contains_aloe=[]
contains_almond=[]
almond_price_list=[]
aloe_price_list=[]

for value in new_list_to_add_Names:
    if "Aloe" in value or "aloe" in value:
        contains_aloe.append(value)
        aloe_price_list.append(new_list_to_add_Sliced_elements[new_list_to_add_Names.index(value)])
    if "Almond" in value or "almond" in value:
        contains_almond.append(value)
        almond_price_list.append(new_list_to_add_Sliced_elements[new_list_to_add_Names.index(value)])

#printing for confirmation
print(contains_aloe)
print(contains_almond)
print(aloe_price_list)
print(almond_price_list)

print(min(aloe_price_list))
print(min(almond_price_list))

#assigining the variables
least_aloe_price=(min(aloe_price_list))
least_almond_price=(min(almond_price_list))

#finding the button to click by xpath
clicking_button=driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
time.sleep(6)

#if least_almond_price in new_list_to_add_Sliced_elements:
clicking_button[new_list_to_add_Sliced_elements.index(least_almond_price)].click()
clicking_button[new_list_to_add_Sliced_elements.index(least_aloe_price)].click()

#clicking on the cart
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

#confirming if it is redirected to cart page
if(driver.current_url=="https://weathershopper.pythonanywhere.com/cart"):
    print("Moisturizer Successfully added to cart")
else:
    print("Failed to add to cart.")

#time to load the things
time.sleep(2)
    
# closing the browser
driver.quit()
