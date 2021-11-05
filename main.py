import time
import threading

import requests

from selenium import webdriver

XPath1 = '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/div[8]/div[2]/div/label[1]/div[1]/div[2]'
XPath11 = '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/div[8]/div[2]/div/label[2]/div[1]/div[2]'
XPath2 = '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/button'
XPath3 = '//*[@id="root"]/div/div[2]/div/div/div/form/div[3]/div[2]/div/div/a'
XPath4 = '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/form/div[5]/div[2]/div/div[1]/div/div/div/div'
XPath5 = '/html/body/div[1]/div[3]/div[3]/div[3]/div/div/form/div[5]/img'
XPath6 = '/html/body/div[1]/div[3]/div[3]/div[3]/div/div/form/div[5]/div/a'

mail = 'randommailgsdfgsdfg4132'
password = 'sjahfkjashdkjh'

sizeArrayLinks = 50

defectUrls = []
index = 45250

def saveCaptchas(*arrayLinks):
    for i in arrayLinks:
        try:
            p = requests.get(i[1])
        except:
            print('Брак', len(defectUrls), i)
            defectUrls.append(i)
            continue
        try:
            with open(f"img/{i[0]}.jpg", "wb") as out:
                out.write(p.content)
                out.close()
        except:
            pass
        print(i[0], i[1])
    print(arrayLinks[-1][0], 'Завершено')
try:
    browser = webdriver.Firefox()
    browser.get('https://account.mail.ru/')
    browser.implicitly_wait(120)
    browser.find_element_by_xpath(XPath3).click()
    browser.implicitly_wait(120)
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(120)
    browser.find_element_by_xpath('//*[@id="fname"]').send_keys('Татьяна')
    browser.find_element_by_xpath('//*[@id="lname"]').send_keys('Каган')
    browser.find_element_by_xpath(XPath1).click()
    browser.find_element_by_xpath('//*[@id="aaa__input"]').send_keys(mail)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    browser.find_element_by_xpath('//*[@id="repeatPassword"]').send_keys(password)
    time.sleep(20)
    browser.find_element_by_xpath(XPath2).click()
    arrayLinks = []
    threads = []
    while True:
        index += 1
        img = browser.find_element_by_xpath(XPath5).get_attribute('src')
        arrayLinks.append((index, img))
        if len(arrayLinks) == sizeArrayLinks:
            thread = threading.Thread(target=saveCaptchas, args=arrayLinks)
            threads.append(thread)
            thread.start()
            arrayLinks = []
        browser.find_element_by_xpath(XPath6).click()
        if index == 50000:
            break
        if index % 1000 == 0:
            browser.delete_all_cookies()
    time.sleep(100)
    for i in threads:
        i.join()
except:
    saveCaptchas(defectUrls)
finally:
    print(defectUrls)
