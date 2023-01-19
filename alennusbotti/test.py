from selenium import webdriver
import time
#alustetaan, mikä sivu avataan
driver = webdriver.Chrome()
#URL:in kohdalle osoite mitä halutaan ostaa
driver.get("https://www.verkkokauppa.com/fi/product/832615/Anker-eufyCam-3-lisakamera-valvontajarjestelmaan")

#Lisätään ostoskoriin
addcart = driver.find_element("xpath", '//*[@id="main"]/section/aside/div[2]/div[2]/div[1]/div[2]/button[1]')
addcart.click()
time.sleep(0.3)
#Siirrytään ostoskoriin
addcart = driver.find_element("xpath", '//*[@id="checkout"]')
addcart.click()

#Siirrytään täyttämään tietoja
time.sleep(0.3)
addcart = driver.find_element("xpath", '//*[@id="main"]/div[2]/div[5]/section/button')
addcart.click()
time.sleep(0.3)

#syötä sähköposti
addcart = driver.find_element("xpath", '//*[@id="login-form-email"]')
addcart.send_keys('KÄYTTÄJÄTUNNUS')

#jatka, syötä salasana ja kirjaudu
addcart = driver.find_element("xpath", '//*[@id="login-button"]')
addcart = driver.find_element("xpath", '//*[@id="login-form-password"]')
addcart.send_keys('SALASANA')
addcart = driver.find_element("xpath", '//*[@id="login-button"]')
addcart.click()
time.sleep(1)
#nextnextnext






