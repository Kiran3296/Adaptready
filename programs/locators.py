from selenium.webdriver import Chrome
from time import sleep

######## id locator #########
driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:www.facebook.com")
# un = driver. find_element("id","email")
# sleep(3)
# un.send_keys("kiran")
# pwd = driver.find_element("id", "pass")
# pwd.send_keys("kiran")
# sleep(2)
# btn= driver.find_element("name","login")
# btn.click()
# sleep(3)
# driver.close()

# driver.get("https://www.lakmeindia.com/")
# sleep(3)
# driver. find_element("partial link text","Skin Dew Satin Lipstick").click()

driver.get("https://www.easemytrip.com/")
sleep(2)
driver. find_element("id","FromSector_show").click()
