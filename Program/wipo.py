####### Testcase for https://www.wipo.int/patinformed/ #############

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import re

driver_path = "../drivers/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.get("https://www.wipo.int/patinformed/")
assert driver.title == 'Pat-INFORMED',"Defect"    #Page title verification
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//input[@class='searchField']").send_keys("sil")
driver.find_element("xpath","//button[@class='green']").click()
search_result = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[3]/ul")))
search_result.click()
op2 = driver.find_element("xpath","//h3[@class='title']")
assert op2.text == 'MACROCYCLIC ANALOGS AND METHODS OF THEIR USE AND PREPARATION','Defect'   #valid box verification
jd= driver.find_element("xpath","//table[@class='patentDetails noBorder'][1]/tr[1]/td[2]")
print(f"Jurisdiction = {jd.text}")
p_date = driver.find_element("xpath","//table[@class='patentDetails noBorder'][1]/tr[3]/td[2]").text
f_date = driver.find_element("xpath","//table[@class='patentDetails noBorder'][1]/tr[4]/td[2]").text
pattern = r"\(.*\)$"
p_date1 = (re.sub(pattern, "", p_date)).rstrip()
f_date1 = (re.sub(pattern, "", f_date)).rstrip()
publication = datetime.strptime(p_date1,"%Y-%m-%d")
filing = datetime.strptime(f_date1,"%Y-%m-%d")
if filing < publication:
    print(f"Publication Date: {p_date}")
    print(f"Filing Date: {f_date}")
else:
    print("Invalid Date")
driver.close()





