from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

# chromepath = "chrome driver path"
# set your chrome driver path here ^

with open('accounts.txt') as f:
    credentials = map(lambda r: tuple(r.split(':')), [row for row in f.read().splitlines()])
for credential in credentials:
    driver = webdriver.Chrome()
    username, password = credential
    url = "https://www.google.com/"
    driver.get(url)

    button1 = driver.find_element_by_xpath('//*[@id="gb_70"]')
    button1.click()
    email = "email"
    # put your email here ^
    login = driver.find_element_by_xpath('//*[@id="identifierId"]')
    login.send_keys(username)
    next0 = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    next0.click()

    passw = WebDriverWait(driver, 5).until(
       EC.presence_of_element_located(('xpath','//*[@id="password"]/div[1]/div/div[1]/input')))

    # put your password here ^
    time.sleep(2)
    passw.send_keys(password)
    time.sleep(3)
    final = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
    final.click()
    print(" ")
    print(Fore.GREEN + ("Logged in to google!"))
    print(" ")
    time.sleep(5)
    yt = "https://www.youtube.com/watch?v=YBqDATEltNE"

    driver.get(yt)
    print(Fore.GREEN + ("started youtube video"))
    print(" ")
    time.sleep(300)
    driver.get(url)

    print(Fore.GREEN + ("starting google searches"))
    print(" ")

    search = driver.find_element_by_xpath('//*[@id="lst-ib"]')
    search.send_keys('cook')

    time.sleep(2)
    search2 = driver.find_element_by_xpath('//*[@id="sbtc"]/div[2]/div[2]/div[1]/div/ul/li[11]/div/span[1]/span/input')
    search2.click()

    searchurl = "https://www.google.com/search?source=hp&ei=IrI6W_e4EMnn5gLloKzgDQ&q=cook&oq=cook&gs_l=psy-ab.12..0j0i131k1j0l4j0i131k1l2j0l2.1514.155452.0.177155.20.5.15.0.0.0.110.250.4j1.5.0....0...1c.1.64.psy-ab..0.20.340...0i10k1.0.wl_aQzdHSe4"

    time.sleep(5)
    first = driver.find_element_by_xpath('//*[@id="rso"]/div[8]/div/div[3]/div[1]/div/h3/a')
    first.click()
    time.sleep(60)
    driver.get(searchurl)

    second = driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div/div/div[1]/h3/div/g-link/a')
    second.click()
    time.sleep(60)
    driver.get(searchurl)
    time.sleep(3)

    third = driver.find_element_by_xpath('//*[@id="rso"]/div[10]/div/div[2]/div[1]/div/h3/a')
    third.click()
    time.sleep(60)
    driver.get(searchurl)
    time.sleep(3)

    fourth = driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
    fourth.click()
    time.sleep(60)
    driver.get(searchurl)
    time.sleep(3)

    last = driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
    last.click()
    driver.get(url)
    print(Fore.GREEN + ("completed google searches"))
    print(" ")
    print(Fore.GREEN + ("{} Done!!").format(username))
    print(" ")
    driver.delete_all_cookies()
    driver.close()

print(Fore.GREEN + "All account done")
