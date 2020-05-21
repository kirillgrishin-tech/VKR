# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

def coordinates(key, plc):
    urll = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": plc, "apikey": key, "format": "json"}
    response = requests.get(urll, params=params)
    response.raise_for_status()
    places_found = response.json()['response']['GeoObjectCollection']['featureMember']
    most_relevant = places_found[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat

def Search(area):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    browser = webdriver.Chrome('C:\\Users\\grish\\Documents\\VKR\\WindMain\\chromedriver.exe',chrome_options=options)
    browser.get("https://yandex.ru/tune/geo?retpath=https%3A%2F%2Flocal.yandex.ru%2F")
    city = browser.find_element_by_id('city__front-input')
    for i in range(30):
        city.send_keys(Keys.BACK_SPACE)
    city.send_keys(area)
    time.sleep(2)
    browser.find_element_by_class_name('b-autocomplete-item__reg').click()
    time.sleep(5)
    sv = browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/div/div/div[2]/div/div/input')
    sv.send_keys(u"свалка"+Keys.ENTER)
    time.sleep(5)
    fgh = browser.find_elements_by_xpath("/html/body/div[2]/div/div[3]/button[2]")
    if len(fgh)>0:
        fgh[0].click()
    time.sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/button/span").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div[4]").click()
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(6)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    loc = browser.find_elements_by_class_name('event-head__location-link')
    a = []
    summ = []
    for i in range(len(loc)):
        a.append(0)
        loc[i] = loc[i].get_attribute("text")
    for i in range(len(loc)):
        if a[i] == 0:
            summ.append([loc[i],0,0,0])
            for p in range(len(loc)):
                if loc[p] == loc[i]:
                    summ[(len(summ)-1)][1] = summ[(len(summ)-1)][1]+1
                    a[p] = 1
    t = 0
    for i in range(len(summ)-1):
        t = i
        maxx = i
        while t<len(summ):
            if summ[t][1] > summ[maxx][1]:
                maxx = t
            t+=1
        buff = summ[i][:]
        summ[i][:] = summ[maxx][:]
        summ[maxx][:]= buff
    key = '02e0341d-e46f-4718-b425-82a41231ad4c'
    for i in range(len(summ)):
        [summ[i][2],summ[i][3]] = coordinates(key,summ[i][0])
    browser.close()
    return summ