from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://formy-project.herokuapp.com/autocomplete")

address_field = driver.find_element(By.ID, "autocomplete")
street_address_field = driver.find_element(By.ID, "street_number")
second_street_address_field = driver.find_element(By.ID, "route")
city_field = driver.find_element(By.ID, "locality")
state_field = driver.find_element(By.ID, "administrative_area_level_1")
postal_code_field = driver.find_element(By.ID, "postal_code")
country_field = driver.find_element(By.ID, "country")

print("All fields were found!")

address_field.send_keys("Random address for address field")
street_address_field.send_keys("Another address")
second_street_address_field.send_keys("Second Another address")
city_field.send_keys("Ivano-Frankivsk")
state_field.send_keys("Nadvirna district")
postal_code_field.send_keys("87123")
country_field.send_keys("Ukraine")

print("Fields updated successfully!")
