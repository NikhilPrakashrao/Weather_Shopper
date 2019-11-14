"""Scope:
Add most expensive sunscreen to the cart
"""
import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#Navigate to the url
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")

#maximize the screen
driver.maximize_window()

#Getting the price of all elements in page
price_of_sunscreen=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")

new_list_to_add_Sliced_elements=[]

for value in price_of_sunscreen:
    print(value.text[-3::])
    new_list_to_add_Sliced_elements.append(value.text[-3::])

print(new_list_to_add_Sliced_elements)
(max(new_list_to_add_Sliced_elements))

#assigining a variable
most_expensive_sunscreen=max(new_list_to_add_Sliced_elements)
print(most_expensive_sunscreen)


if most_expensive_sunscreen in new_list_to_add_Sliced_elements:
    saving_index=new_list_to_add_Sliced_elements.index(most_expensive_sunscreen)
print(saving_index)

#finding the button to be clicked
clicking_button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')

#Clicking_button
clicking_button[new_list_to_add_Sliced_elements.index(most_expensive_sunscreen)].click()

#clicking on the cart
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

#confirming that it is redirected to the checkout page
if(driver.current_url=="https://weathershopper.pythonanywhere.com/cart"):
    print("Most expensive Sunscreen Successfully added to cart")
else:
    print("Failed to add to cart.")
    
#time to load things.
time.sleep(3)

# close the browser
driver.quit()