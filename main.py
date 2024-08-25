from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
url_Flight_Club="create youre google form"
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup=BeautifulSoup(response.content,"html.parser")
#first we get all the link of all places
links=soup.find_all(name="a",class_="StyledPropertyCardDataArea-anchor")
list_link=[]
for link in links:
    list_link.append(link.get("href"))
print(list_link)
#get all prices per month of each place
prices=soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

price_list=[]
for price in prices:
    price_list.append(price.text.split("+")[0].split("/")[0])
print(price_list)
address=soup.find_all(name="address")
address_list=[]
for add in address:
    address_list.append(add.text.split("|")[0].strip())
print(address_list)
#here we use selenium to fill the form
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#use xpath to select the short answer in google form
for i in range(len(list_link)):
    driver.get(url_Flight_Club)
    time.sleep(2)
    type_address=driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month=driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link=driver.find_element(By.XPATH,
                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    type_address.send_keys(address_list[i])
    price_per_month.send_keys(price_list[i])
    link.send_keys(list_link[i])
    time.sleep(1)
    submit=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()




    
