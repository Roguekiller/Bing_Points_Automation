import time
import random
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#List to auto type in different searchs.
searchList = ['ran', 'sing', 'birds', 'cows', 'life', 'rabbit', 'dancing', 'sleep',
              'dark', 'light', 'water', 'earth', 'fire', 'air', 'long', 'ago', 'the',
              'four', 'nations', 'lived', 'together', 'in', 'harmony', 'then', 'everything',
              'changed', 'when', 'the', 'fire', 'nation', 'attacked']

#Fields for Live Login
EmailField = (By.ID, "i0116")
PasswordField = (By.ID, "i0118")
NextButton = (By.ID, "idSIButton9")


#Function to create tab and initiate searches
#Logs into account for Live Login based off of the users credentials.
def Search():
    #Edit executable_path with = r'(Full File path where geckodrive.exe is located)'
    driver = webdriver.Firefox(executable_path = r'')
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1604356127&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d12BA25AD0C50655810CA2ADB0DF7640F&lc=1033&id=264960&CSRFToken=20c21f6c-f17c-478a-b3cc-6fb670ba8e5a&aadredir=1")

    #Enter Email in "" eg. send.keys("meWhoAngyou.aol.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EmailField)).send_keys("")

    #Click Next
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NextButton)).click()

    #Enter Password in "" eg. send.keys("theAvatarIntroisIntheLIST")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PasswordField)).send_keys("")
    
    #Click Next
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NextButton)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NextButton)).click()

    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
    time.sleep(4)
    
    #User defined searchs per day. Edit for more searchs.
    for i in range(5):
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(str(searchList[random.randrange(31)]) + " " + str(searchList[random.randrange(31)]) + " " + str(searchList[random.randrange(31)]))
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

        
        time.sleep(random.randrange(5, 20))
        #Create a new tab within same Firefox Window
        body = driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')

    #Confirm close program
    print("Completed Execution. Finished? (Y/N)")
    confirm = input()
    if confirm == 'y' or confirm == 'Y':
         driver.close()
    elif confirm == 'n' or confirm == 'N':
        print("Complete.")

#End both tasks that are called. Firefox/Python task.
def TaskKills():
    os.system("TASKKILL /F /IM geckodriver.exe")
    os.system("TASKKILL /F /IM pythonw.exe")
    
#Main: Starts the program
Search()
TaskKills()
