from time import sleep
from selenium import webdriver

browser = webdriver.Chrome('C:\driver\chromedriver.exe')

browser.get("http://localhost/dddd/index.php%22)

idk=browser.find_element_by_name("id")
imie=browser.find_element_by_name("imie")
nazwisko=browser.find_element_by_name("nazwisko")
miasto=browser.find_element_by_name("miasto")

idk.send_keys('ABCF')
sleep(2)
imie.send_keys('Piotr')
sleep(2)
nazwisko.send_keys('Kowal')
sleep(2)
miasto.send_keys('Poniatowa')

button1=browser.find_element_by_id("s1")
sleep(5)
button1.click()

browser.close()