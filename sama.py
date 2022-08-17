import datetime
from typing import final
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select


#getting today date for saving files
x = datetime.datetime.now()
print(x)
today = "2021-" +x.strftime("%m")+"-" +x.strftime("%d")
print(today)

from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver_path = "C:\\Users\\mohan_\\DEVS\\webDrivers\\chromedriver.exe"
driver = webdriver.Chrome(options = options, executable_path = driver_path)
driver.get("https://www.sama.gov.sa/en-US/pages/default.aspx")


driver.implicitly_wait(5) # seconds

#gold 
gold = driver.find_element_by_xpath("//span[contains(text(),'Gold')]").text
gold_price = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[5]/div[7]/span[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[4]    ").text
print( gold+ " : " +gold_price )


silver= driver.find_element_by_xpath("//span[contains(text(),'Silver')]").text 
silver_price = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[5]/div[7]/span[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[4]").text
#selver 
print(silver+ " : " + silver_price)


oil = driver.find_element_by_xpath("//span[contains(text(),'Oil')]").text
oil_price = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[5]/div[7]/span[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[4]").text
#oil 
print(oil + " : " +oil_price )


with open("D:\\DEVS\\Docker\\DEV\\SAMA\\"+"prises as date " +today+".txt", "w") as text_file:
    text_file.write(gold + " : "+ gold_price + "\n" + silver + " : " + silver_price+ "\n" +oil + " : "+ oil_price+ "\n")

driver.quit()


