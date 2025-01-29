from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Get search query from user
query = input("Enter your search query: ")

# Open Google
driver.get("https://www.google.com")

# Find the search box and enter query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(2)

# Extract search results (titles & URLs)
results = driver.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')

search_data = []
for result in results:
    try:
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        link = result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        search_data.append(f"{title}\n{link}\n")
    except:
        pass  # Skip results that don't follow the expected structure

# Save results to a file
with open("results.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join(search_data))

# Print results to console
print("\nTop search results:")
print("\n".join(search_data))

# Close the browser
driver.quit()
