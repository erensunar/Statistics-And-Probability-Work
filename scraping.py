from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import json
import time

liste = []

driver = webdriver.Chrome('./chromedriver')
url = "https://www.trendyol.com/sr?wb=102323&qt=lenovo&st=lenovo&lc=106084&os=1"
driver.get(url)

time.sleep(3)

urunler = driver.find_elements(By.CLASS_NAME,"p-card-wrppr" )



urunSayisi = len(urunler)
yeniUrunSayisi = 0
while urunSayisi != yeniUrunSayisi:
    urunSayisi = yeniUrunSayisi
    pyautogui.press("down", presses=80)
    time.sleep(3)
    urunler = driver.find_elements(By.CLASS_NAME,"p-card-wrppr" )
    yeniUrunSayisi = len(urunler)








for urun in urunler:
    dict = {"isim" : "",
        "fiyat": "",
        }
    urunIsmi = urun.find_element(By.CLASS_NAME, "prdct-desc-cntnr-name").text
    
    urunFiyat = urun.find_element(By.CLASS_NAME, "prc-box-dscntd").text
    virgulKonum = urunFiyat.find(",")
    if virgulKonum >0:
        urunFiyat = urunFiyat[:virgulKonum]
    else:
        spaceLocation =  urunFiyat.find(" ")
        urunFiyat = urunFiyat[:spaceLocation]
    
    urunFiyat = urunFiyat.replace(".", "")

    dict["isim"] = urunIsmi
    dict["fiyat"] = urunFiyat
    liste.append(dict)

with open('data.json', 'w') as fp:
    json.dump(liste, fp)