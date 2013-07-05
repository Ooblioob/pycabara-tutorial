from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://www.google.com/xhtml')
driver.save_screenshot('google_homepage.png')  # This saves the 'screen shot'
search_box = driver.find_element_by_name('q')
search_box.send_keys('PhantomJS WebDriver')
search_box.submit()
driver.save_screenshot('google_results_PhantomJS_WebDriver.png')
driver.quit()
