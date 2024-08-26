from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#driver = webdriver.Chrome()
driver.get("http://ubuntu-test.devops.org:8085/contact.html")
print(driver.title)

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[1]/div/div[1]/div[1]/div/input').send_keys("Rajasekhar Gajula")
driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[1]/div/div[1]/div[2]/div/input').send_keys("1234567890")
driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[1]/div/div[2]/input').send_keys("rajasekhar@gajula.com")
driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[1]/div/div[3]/input').send_keys("Hi, How are you? trying to reaching you.")
driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[1]/div/div[4]/button').click()
#print(driver.find_element(By.ID, 'message').text)

driver.close()
