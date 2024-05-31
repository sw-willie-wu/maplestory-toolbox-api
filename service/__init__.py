import json
from urllib import parse

import requests
from bs4 import BeautifulSoup


def crawl_img(event_name):
    event_api = 'https://maplestory.beanfun.com/api/GamaAd/FindAdData?AdType=MainBannerPC'

    soup = BeautifulSoup(requests.get(event_api).content, 'lxml')
    events = json.loads(soup.select('p')[0].string)['listData']
        
    for event in events:

        if event['adName'].strip().split('】')[0][1:] != event_name:
            continue

        with requests.session() as s:
            res = s.get(event['adUrl'])
            head = s.head(event['adUrl'])
            soup = BeautifulSoup(res.content, 'lxml')

            bid = res.url.split('=')[1]
            token = soup.select('input[name=__RequestVerificationToken]')[0]['value']
            form_data = {"Bid":bid}
            data = parse.urlencode(form_data)

            headers = {
                # 'Accept': '*/*',
                # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                # 'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
                # 'Content-Length': '9',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'X-Csrf-Token': token,
                # 'X-Requested-With': 'XMLHttpRequest'
            }

            content = s.post(
                url='https://maplestory.beanfun.com/bulletin?handler=BulletinDetail',
                data=data,
                headers=headers
            )

            data = json.loads(content.text)
            soup = BeautifulSoup(data['data']['myDataSet']['table']['content'], 'lxml')
            img_url = soup.select('img')[0]['src']
        
        break
            
    return {
        'name': event['adName'].strip().split('】')[1].strip(), 
        'start_time': event['adsTime'], 
        'end_time': event['adeTime'], 
        'img': img_url
    }