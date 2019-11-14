"""
Add two sunscreens to your cart. 
First, select the least expensive sunscreen that is SPF-50. For your second sunscreen, 
select the least expensive sunscreen that is SPF-30. 
Click on the cart when you are done
"""

import time
from selenium import webdriver

#Launch the chrome browser
driver=webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to URL
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")

# Finding price of sunscreen by xpath
price_of_sunscreen=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")

new_list_to_add_Sliced_elements=[]

for value in price_of_sunscreen:
    print(value.text[-3::])
    new_list_to_add_Sliced_elements.append(value.text[-3::])
print(new_list_to_add_Sliced_elements)

# Finding names of sunscreen by xpath
names_of_sunscreen=driver.find_elements_by_xpath("//p[@class='font-weight-bold top-space-10']")

new_list_to_add_Names=[]
for value in names_of_sunscreen:
    print("The value is",value.text)
    new_list_to_add_Names.append(value.text)
print(new_list_to_add_Names)


with_spf_50=[]
with_spf_30=[]
spf_30_price_list=[]
spf_50_price_list=[]

for value in new_list_to_add_Names:
    if "SPF-50" in value :
        with_spf_50.append(value)
        spf_50_price_list.append(new_list_to_add_Sliced_elements[new_list_to_add_Names.index(value)])
    if "spf-30" in value or "SPF-30" in value:
        with_spf_30.append(value)
        spf_30_price_list.append(new_list_to_add_Sliced_elements[new_list_to_add_Names.index(value)])

#printing values for confirmation
print(with_spf_50)
print(with_spf_30)
print(spf_50_price_list)
print(spf_30_price_list)

print(min(spf_50_price_list))
print(min(spf_30_price_list))

#assigining variables for the items
spf_50_price=(min(spf_50_price_list))
spf_30_price=(min(spf_30_price_list))

# finding the buttons to click by xpath
clicking_button=driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
time.sleep(2)

# clicking on the buttons
clicking_button[new_list_to_add_Sliced_elements.index(spf_50_price)].click()
clicking_button[new_list_to_add_Sliced_elements.index(spf_30_price)].click()

time.sleep(2)

#clicking on the cart
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

#confirming that it is redirected to the checkout page

if(driver.current_url=="https://weathershopper.pythonanywhere.com/cart"):
    print("Sunscreens Successfully added to cart")
else:
    print("Failed to add to cart.")

#time to load the things
time.sleep(2)
    
# closing the browser
driver.quit()
