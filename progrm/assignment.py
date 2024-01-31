from selenium.webdriver import Chrome
from time import sleep
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element("link text", "Register").click()
sleep(2)
driver.find_element("id", "gender-female").click()
driver.find_element("id", "FirstName").send_keys("Kiran")
sleep(2)
driver.find_element("id", "LastName").send_keys("Sahoo")
sleep(2)
driver.find_element("id", "Email").send_keys("kiransahoo112@gmail.com")
sleep(2)
driver.find_element("id", "Password").send_keys("Pythonselenium")
sleep(2)
driver.find_element("id", "ConfirmPassword").send_keys("Pythonselenium")
sleep(2)
driver.find_element("id", "register-button").click()
sleep(2)
driver.close()



