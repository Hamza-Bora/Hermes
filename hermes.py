#!/usr/bin/python3
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


print('\033[31m'+"""
 _____ __   _ _______ _______ _______      ______   _____  _______
   |   | \  | |______    |    |_____|      |_____] |     |    |
 __|__ |  \_| ______|    |    |     |      |_____] |_____|    |

"""+'\033[0m')

print('\033[31m'+"""
                o#'9MMHb':'-,o,
            .oH":HH$' "' ' -*R&o,
            dMMM*""'`'      .oM"HM?.
            ,MMM'          "HLbd< ?&H\                  
        .:MH ."\          ` MM  MM&b                    
        . "*H    -        &MMMMMMMMMH:              
        .    dboo        MMMMMMMMMMMM.
        .   dMMMMMMb      *MMMMMMMMMP.
        .    MMMMMMMP        *MMMMMP .
            `#MMMMM           MM6P ,
        '    `MMMP"           HM*`,
            '    :MM             .- ,
            '.   `#?..  .       ..'
                -.   .         .-
                -.oo,oo.-

"""+'\033[0m')
print(7*"\t"+'\033[7m'+"@Hamza_Bora"+'\033[0m')



#from stack overflow 
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#----------------------------------------------------------------

#Step 1 (Login Account);

username1 = input("Username : ")
password1 = input("Password : ")

if bool(username1) == False or bool(password1) == False:
	username1 = "your username"
	password1 = "your password"
	print("Standart user.")



driver = webdriver.Chrome(executable_path=r'chromedriver yolu')
driver.get('https://www.instagram.com')

driver.implicitly_wait(20)

username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')

username.send_keys(username1)
password.send_keys(password1)
login_button.click()
#time.sleep(4)
print("Connected.")

#For notification tab pass
next1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]') 
next1.click()
print("Notification tab passed.")

#for enter the your account page
driver.get('https://www.instagram.com/'+username1)

#Storys click;

story_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div') # Xpath code of storys button
story_button.click()


timer = 1
xpath = "4" # for changing xpath value(first 4, after 3)
x_change = True #boolen variable for changing xpath value
photo_yedek = ""

while True:
	
	dorulama = True
	print("while", timer)

	if x_change != True:
		xpath = "3"
	
	#viewer's photo;
	viewer_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/div[3]/div[2]/button/div/div')
	viewer_button.click()

	try:

		photo = driver.find_element_by_xpath('/html/body/div['+xpath+']/div/div/div[2]/div/div/div[1]/div[1]/a/img').get_attribute("src") #link of profile photo
		print('\033[31m'+photo+'\033[0m')

		if photo == photo_yedek:
			print("FARKLI KISI BEKLENIYOR..")
			time.sleep(6)  #time.sleep() / for not ban !
			x_change = False
			driver.refresh() #refresh because for new viewers
			continue


	except Exception as e:
		print("Error the airse")
		dorulama = False
		print(dorulama)

	if dorulama == True:
		urllib.request.urlretrieve(photo, "image"+str(timer)+".png")
		print("İmage Download. image number", timer)
		os.system(f"./bot.py {timer}")
		timer+=1

	photo_yedek = photo #for not to share the same photo
	driver.refresh()
	x_change = False
