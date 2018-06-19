from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://admin.daokoujihua.com/')
adminelement = driver.find_element_by_id('username');
adminelement.send_keys("admin");
passwordelement = driver.find_element_by_id('password');
passwordelement.send_keys("admin");
driver.find_element_by_class_name('login').click()
driver.find_elements_by_css_selector()
driver.find_elements()