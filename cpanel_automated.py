from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(20) # seconds

driver.get("https://a2plcpnl0198.prod.iad2.secureserver.net:2083/cpsess5191920891/frontend/paper_lantern/filemanager/upload-ajax.html?file=&fileop=&dir=%2Fhome%2Fol4sa8s89yyu%2Fpublic_html&dirop=&charset=&file_charset=&baseurl=&basedir=")

driver.find_element_by_id("user").send_keys("ENTER USERNAME")
driver.find_element_by_id ("pass").send_keys("ENTER PASSWORD")
driver.find_element_by_id("login_submit").click()

driver.find_element_by_id("uploader_file_input").send_keys(r"C:\Users\michael.b.martinez\Desktop\mm1172019\Scoreboard.csv")

driver.find_element_by_class_name("default").click()
try:
    driver.find_element_by_class_name("default").click()
except:
    print('okay')
    
driver.find_element_by_id("uploader_file_input").send_keys(r"C:\Users\michael.b.martinez\Desktop\mm1172019\test.png")
driver.find_element_by_class_name("default").click()


try:
    driver.find_element_by_class_name("default").click()
except:
    driver.quit()
