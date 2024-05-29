import time
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def crawl_img(event_name):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')

    chrome = webdriver.Firefox(options=options)
    chrome.get("https://maplestory.beanfun.com/main")
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    soup = BeautifulSoup(chrome.page_source, "lxml")

    # get events
    events = soup.select("a.mBulletin-slide2-item")
    for event in events:
        title = event.select("div.mBulletin-slide2-title")[0].get_text().strip().split("】")
        title[0] = "【" + title[0] if title[0][0] != "【" else title[0]

        if title[0][1:] == event_name: 
            utime = datetime.strptime(event.select("div.mBulletin-slide2-date")[0].get_text(), '%Y.%m.%d')
            href = event.get("href")
            chrome.get(f"{href}")
            time.sleep(1)
            chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            event_page = BeautifulSoup(chrome.page_source, "lxml")
            img_url = event_page.select("div.mBulletin-content > p > img")[0].get("src")
            break
            
            # print(title[1], img_url)
        time.sleep(1)
    chrome.quit()
    return title[1], img_url