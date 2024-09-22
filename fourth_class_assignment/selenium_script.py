import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#1
# URLs to open
urls = {
    "Chrome": "http://www.walla.co.il",
    "Firefox": "http://www.ynet.co.il"
}

# Open in Chrome
webbrowser.get("google-chrome").open(urls["Chrome"])

# Open in Firefox
webbrowser.get("firefox").open(urls["Firefox"])

#2
# Initialize the browser
driver = webdriver.Firefox()

# Open the website
url = "http://www.walla.co.il"
driver.get(url)

# a. Create a variable with the website's title
expected_title = driver.title
print(f"Expected Title: {expected_title}")

# b. Refresh the website
driver.refresh()
time.sleep(2)  # Wait for a moment to let the page reload

# c. Get the website name and compare it to the variable created
current_title = driver.title
print(f"Current Title: {current_title}")

if current_title == expected_title:
    print("The titles match!")
else:
    print("The titles do not match.")

# Close the browser
driver.quit()

#3 - Yes, the elements are the same.

#4
try:
    # Open Google Translate
    driver.get("https://translate.google.com")

    # Allow some time for the page to load
    time.sleep(2)

    # Locate the input text area (XPath may vary)
    text_area = driver.find_element(By.XPATH, "//textarea[@aria-label='Source text']")

    # Write Hebrew text in the text area
    hebrew_text = "שלום עולם"  # "Hello World" in Hebrew
    text_area.send_keys(hebrew_text)

    # Allow some time to see the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()


#5
try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Allow some time for the page to load
    time.sleep(2)

    # Locate the search box
    search_box = driver.find_element(By.NAME, "search_query")

    # Type the name of a song (e.g., "Imagine - John Lennon")
    song_name = "Imagine - John Lennon"
    search_box.send_keys(song_name)

    # Locate and click the search button
    search_button = driver.find_element(By.ID, "search-icon-legacy")
    search_button.click()

    # Allow some time to see the search results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

#6
try:
    # Open Google Translate
    driver.get("https://translate.google.com")

    # Allow some time for the page to load
    time.sleep(2)

    # 1. Locate the translation text field using XPath
    translation_field_xpath = driver.find_element(By.XPATH, "//textarea[@aria-label='Source text']")
    print("Element found using XPath:", translation_field_xpath)

    # 2. Locate the translation text field using CSS Selector
    translation_field_css = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='Source text']")
    print("Element found using CSS Selector:", translation_field_css)

    # 3. Locate the translation text field using name attribute
    translation_field_name = driver.find_element(By.NAME, "text")
    print("Element found using Name:", translation_field_name)

    # Allow some time to see the results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

#7
email = "your-email@example.com"
password = "your-password"

try:
    # Open Facebook login page
    driver.get("https://www.facebook.com/")

    # Allow time for the page to load
    time.sleep(2)

    # Find the email input field and enter the email
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(email)

    # Find the password input field and enter the password
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys(password)

    # Find the login button and click it
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Allow some time to see the result or ensure login
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

#8
try:
    # Open any webpage (for example, Google)
    driver.get("https://www.google.com")

    # Allow time for the page to load
    time.sleep(2)

    # Print cookies before deletion
    print("Cookies before deletion:")
    cookies_before = driver.get_cookies()
    print(cookies_before)

    # Delete all cookies
    driver.delete_all_cookies()

    # Allow some time for the action to complete
    time.sleep(2)

    # Verify and print cookies after deletion
    print("\nCookies after deletion:")
    cookies_after = driver.get_cookies()
    print(cookies_after)

    # Check if all cookies were successfully deleted
    if len(cookies_after) == 0:
        print("\nAll cookies have been deleted successfully.")
    else:
        print("\nSome cookies are still present.")

finally:
    # Close the browser
    driver.quit()

#9
try:
    # Open the GitHub website
    driver.get("https://github.com/")

    # Allow some time for the page to load
    time.sleep(2)

    # Locate the search field by name attribute
    search_box = driver.find_element(By.NAME, "q")

    # Type "Selenium" in the search field
    search_box.send_keys("Selenium")

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Allow some time to view the search results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

#10
# Create ChromeOptions object to disable extensions
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--incognito")  # Optionally open in incognito mode

# Initialize the Chrome browser with options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open any webpage (e.g., Google)
    driver.get("https://www.google.com")

    # Wait to see the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
