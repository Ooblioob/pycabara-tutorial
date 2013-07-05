import time
from selenium import webdriver

# This is a smoke test
# It can help ensure that Selenium and the Chrome webdriver are installed properly

driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.

# Let's go to the Google homepage
driver.get('http://www.google.com/xhtml')

# Add a delay to let you see it
time.sleep(5)

# Find the search text box and enter the text to search with.
search_box = driver.find_element_by_name('q')
search_box.send_keys('pycabara')

# Now, press the page submit associated with the text box (the "search" button).
search_box.submit()

# Another delay to let you see it
time.sleep(5)

# Close the Selenium driver.
driver.quit()
