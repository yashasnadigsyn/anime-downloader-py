from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

animename = input('Please enter the name of the anime:')
episode = input("Enter episode number:")
print("SIT BACK AND RELAX!!!")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.get("https://animeflix.sbs")
delay = 15
sleep(5)
# searchbutton = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[7]/i')))
# searchbutton.click()
searchspace = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID, 'livesearch')))
searchspace.click()
sleep(1)
searchspace.send_keys(animename)
sleep(3)
searchspace.send_keys(Keys.ENTER)
sleep(10)

animelinkslist = []
animenames = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'film-name')))
a=0
for i in animenames:
    if a == 8:
        break
    a = a+1
    print(f"{i.text} --------------> {a}")
    animelinksname = WebDriverWait(i, delay).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
    for j in animelinksname:
        animelinkslist.append(j.get_attribute('href'))

animechoice = int(input("Please choose your index number:"))
animechoice = animelinkslist[animechoice-1]
animechoice = animechoice[0:22] + "watch" + animechoice[22+5: ]
animechoice += f"-episode-{episode}"
driver.get(animechoice)
sleep(10)
download = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/a')))
download.click()
sleep(10)
print("Please click on this link to download your preffered version: "+ driver.current_url)


