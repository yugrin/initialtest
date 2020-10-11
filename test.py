import selenium
import time
from selenium import webdriver
#PATH = "C:\Users\yugan\AppData\Local\Microsoft\WindowsApps\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:4000/")
#driver.get("https://accounts.google.com/signin/v2/challenge/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=googlemail&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession&cid=1&navigationDirection=forward&TL=AM3QAYZwG_hV8TxVzqmz8rb7nYN_uR44mhJcwAhc5i0vXC6e0uqOKp9r-hZztNXC")

time.sleep(5)
#driver.find_element_by_id("username").send_keys('yugandhara.tawde')
#driver.find_element_by_id("identifierNext").click()
driver.find_element_by_name("username").send_keys('admin')
driver.find_element_by_name("password").send_keys('password')
time.sleep(10)
driver.find_element_by_name("submit").click()
time.sleep(20)
#driver.find_element_by_id("password").send_keys('yugsriN31911@')
#driver.find_element_by_id("login").click()
#time.sleep(5)

#driver.get("https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")
#driver.find_element_by_xpath('//button[normalize-space()="Sign out"]').click()
driver.close()