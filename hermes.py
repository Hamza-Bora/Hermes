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



#stack overflow 'dan aldığım kod bloğu //yoksa kod hata veriyordu.
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

#Bildirim sekmesini geçmek için;
next1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]') 
next1.click()
print("Notification tab passed.") #Bildirim sekmesi geçildi.

#Kendi bot hesabının profiline girme;

driver.get('https://www.instagram.com/'+username1)

#Storys click;

story_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div') # Xpath code of storys button
story_button.click()


timer = 1
xpath = "4" # Bu xpath değeri ilk storye girdiğinde 4 sonrasında 3 oluyor o yüzden böyle bir değişkene ihtiyaç duydum.
x_change = True #xpath değerini değiştirmem için gerekli olan boolean değişkeni
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

    photo = driver.find_element_by_xpath('/html/body/div['+xpath+']/div/div/div[2]/div/div/div[1]/div[1]/a/img').get_attribute("src") #profil fotorafın linki
    print('\033[31m'+photo+'\033[0m') #linki ekrana bastırmayı tercih ettim

    if photo == photo_yedek:
          print("FARKLI KISI BEKLENIYOR..")
          time.sleep(6)  #time.sleep() 'e almazsanız kısa süre sonra instagram driverı engelliyor.
	  x_change = False
          driver.refresh() #yeniledik çünkü storye yeni giren kullanıcıları kaçırmayalım
          continue
    

  except Exception as e:
    print("airse hatası")
    dorulama = False
    print(dorulama)

  if dorulama == True:
        urllib.request.urlretrieve(photo, "resim"+str(timer)+".png")
        print("İmage Download. image number", timer)
        os.system(f"./bot.py {timer}") #upload için scripti çalıştırma komutu timer değişleni ise resim.png dosyasının kaçıncı resim olacağını belirtiyor meslea(resim5.png)
        timer+=1

  photo_yedek = photo #eski photo değişkenine ihtiyacımız var çünkü önceki ile aynı olursa birden fazla aynı fotografı basabilir
  driver.refresh()
  x_change = False
