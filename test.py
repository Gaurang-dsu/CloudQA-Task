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
    firstname_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fname']")))
    print("First Name field found")
    firstname_field.send_keys("John")
except Exception as e:
    print(f"Error entering First Name: {e}")

try:
    lastname_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='lname']")))
    print("Last Name field found")
    lastname_field.send_keys("Doe")
except Exception as e:
    print(f"Error entering Last Name: {e}")

try:
    gender_male = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Male']")))
    print("Gender Male option found")
    gender_male.click()
except Exception as e:
    print(f"Error selecting Gender: {e}")

# Optional: Submit the form
try:
    submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    submit_button.click()
    print("Form submitted successfully")
except Exception as e:
    print(f"Error clicking submit button: {e}")

# Wait to observe the form submission
time.sleep(5)

# Close the browser
driver.quit()
