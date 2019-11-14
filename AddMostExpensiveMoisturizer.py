"""Scope:
Add most expensive moisturizer to the cart
"""
import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#Navigate to the url
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

#maximize the screen
driver.maximize_window()

#Getting the price of all elements in page
price_of_moisturizer=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")

new_list_to_add_Sliced_elements=[]

for value in price_of_moisturizer:
    print(value.text[-3::])
    new_list_to_add_Sliced_elements.append(value.text[-3::])

print(new_list_to_add_Sliced_elements)
(max(new_list_to_add_Sliced_elements))

#assigining a variable
most_expensive_moisturizer=max(new_list_to_add_Sliced_elements)
print(most_expensive_moisturizer)


if most_expensive_moisturizer in new_list_to_add_Sliced_elements:
    saving_index=new_list_to_add_Sliced_elements.index(most_expensive_moisturizer)
print(saving_index)

#finding the button to be clicked
clicking_button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')

#Clicking_button
clicking_button[new_list_to_add_Sliced_elements.index(most_expensive_moisturizer)].click()

#clicking on the cart
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

#confirming that it is redirected to the checkout page
if(driver.current_url=="https://weathershopper.pythonanywhere.com/cart"):
    print("Most expensive Moisturizer Successfully added to cart")
else:
    print("Failed to add to cart.")
    
#time to load things.
time.sleep(3)

# close the browser
driver.quit()