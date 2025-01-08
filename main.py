# Import necessary libraries for Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options with user-agent and detach option
options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver with configured options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the target website (neuralnine.com)
driver.get("https://www.neuralnine.com/")

# Find all links on the page using XPath
links = driver.find_elements(By.XPATH, "//a[@href]")

# Loop through each link
for link in links:
    # Check if the link's innerHTML contains "Books"
    if "Books" in link.get_attribute("innerHTML"):
        # Click the link if it contains "Books"
        link.click()
        # Exit the loop after clicking the first "Books" link (assuming we only want one)
        break

# Define the XPath to find book links with "7 IN 1" title and 2 links
book_links_xpath = "//div[contains(@class,'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a"

# Find book links matching the XPath criteria
book_links = driver.find_elements(By.XPATH, book_links_xpath)

# Print the URLs of the found book links
for book_link in book_links:
    print(book_link.get_attribute("href"))

# Click the first book link in the list (assuming we only want one)
book_links[0].click()

# Switch focus to the newly opened window (likely the book page)
driver.switch_to.window(driver.window_handles[1])

# Introduce a short wait (3 seconds) for the page to load (adjust as needed)
time.sleep(3)

# Define the XPath to find buttons containing "Paperback" and "$"
buttons_xpath = "//a[.//span[contains(text(),'Paperback')] and .//span[contains(text(),'$')]]"

# Find all buttons matching the XPath criteria
buttons = driver.find_elements(By.XPATH, buttons_xpath)

# Initialize an empty list to store extracted prices
prices = []

# Loop through each button
for button in buttons:
    # Find the element containing the price information within the button (assuming it's within a span with class "slot-price")
    price_element = button.find_element(By.XPATH, ".//span[@class='slot-price']")
    # Extract the actual price text from within the price element (assuming it's within a span with classes "a-size-base" and "a-color-secondary")
    price_text = price_element.find_element(By.XPATH, ".//span[@class='a-size-base a-color-secondary']").text
    # Append the extracted price text to the prices list
    prices.append(price_text)

# Print the extracted prices (price including the dollar sign)
for price in prices:
    print(price)

# Close the browser window (optional)
# driver.quit()