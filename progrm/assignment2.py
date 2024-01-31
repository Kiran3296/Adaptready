######### REGISRATION FOR PASSPRT SEVA ###########

from selenium.webdriver import Chrome
from time import sleep
driver = Chrome()
driver.get("https://www.passportindia.gov.in/AppOnlineProject/welcomeLink#")
driver.maximize_window()
sleep(3)
driver.find_element("xpath","//div[@class='main_button_typ_002']").click()
sleep(1)
driver.find_element("xpath","//option[.='Ahmedabad']").click()
sleep(1)
driver.find_element("xpath","//input[@name='givenName']").send_keys("pikachu")
sleep(1)
driver.find_element("xpath","//input[@name='surname']").send_keys("pokemon")
sleep(1)
driver.find_element("xpath","//input[@name='dob']").send_keys("19/08/2023")
sleep(1)
driver.find_element("xpath","//input[@name='email']").send_keys("weblitese@gmail.com")
sleep(1)
driver.find_element("xpath","//label[@for='emailloginSameyes']").click()
sleep(1)
driver.find_element("xpath","//input[@id='loginId']").send_keys("SOHAIL3596")
sleep(1)
driver.find_element("xpath","//input[@id='pwd']").send_keys("SOHAIL3596")
sleep(1)
driver.find_element("xpath","//input[@id='confirmPwd']").send_keys("SOHAIL3596")
sleep(1)
driver.find_element("xpath","//option[.='Birth City']").click()
sleep(1)
driver.find_element("xpath","//input[@name='hintAns']").send_keys("goa")
sleep(20)
driver.find_element("xpath","//input[@name='register']").click()
sleep(2)
driver.close()

##################### SPOTIFY REGISTRATION ########################
driver.get("https://www.spotify.com/in-en/free/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath","//a[.='Sign up']").click()
driver.find_element("xpath","//input[@id='email']").send_keys("1234567890")
sleep(1)
driver.find_element("xpath","//input[@id='password']").send_keys("spotify123")
sleep(1)
driver.find_element("xpath","//input[@id='displayname']").send_keys("kk95")
sleep(1)
driver.find_element("xpath","//input[@id='year']").send_keys("1996")
sleep(1)
driver.find_element("xpath","//option[.='May']").click()
sleep(1)
driver.find_element("xpath","//input[@id='day']").send_keys("1")
sleep(1)
driver.find_element("xpath","//span[.='Female']").click()
sleep(1)
driver.find_element("xpath","//span[contains(.,'I would prefer not to')]").click()
sleep(2)
driver.find_element("xpath","//span[contains(.,'registration')])[2]").click()
sleep(2)
driver.find_element("xpath","//span[.='Sign up']").click()
sleep(2)
driver.close()

























