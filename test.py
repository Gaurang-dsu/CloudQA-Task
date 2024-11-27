from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

# Wait for the elements to be visible
wait = WebDriverWait(driver, 10)

try:
    # Find First Name field by a flexible locator (placeholder and name as fallbacks)
    firstname_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name' or @name='First Name']"))
    )
    print("First Name field found")
    firstname_field.send_keys("Gaurang")
except Exception as e:
    print(f"Error entering First Name: {e}")

try:
    # Find Last Name field by a flexible locator
    lastname_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Last Name' or @name='Last Name']"))
    )
    print("Last Name field found")
    lastname_field.send_keys("Goyal")
except Exception as e:
    print(f"Error entering Last Name: {e}")

try:
    # Find Gender Male option using flexible locator
    gender_male = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='Male']"))
    )
    print("Gender Male option found")
    gender_male.click()
except Exception as e:
    print(f"Error selecting Gender: {e}")

# Submit the form
try:
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit') or @type='submit']"))
    )
    submit_button.click()
    print("Form submitted successfully")
except Exception as e:
    print(f"Error clicking submit button: {e}")

# Wait to observe the form submission
time.sleep(5)

# Close the browser
driver.quit()
