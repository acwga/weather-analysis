import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}

data = [] # 存储爬取的数据

def crawl_weather(province_url):
    try:
        response = requests.get(province_url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        # 天气表格
        rows = soup.select("table tr")
        for row in rows[2:]: # 跳过前两行表头
            tds = row.find_all("td")
            if len(tds) == 8:
                city = tds[0].text.strip()
                weather = tds[4].text.strip()
                high_temp = tds[3].text.strip()
                low_temp = tds[6].text.strip()
                data.append([city, weather, high_temp, low_temp])

            if len(tds) == 9:
                city = tds[1].text.strip()
                weather = tds[5].text.strip()
                high_temp = tds[4].text.strip()
                low_temp = tds[7].text.strip()
                data.append([city, weather, high_temp, low_temp])
        
        time.sleep(random.uniform(1, 3)) # 避免请求过快

    except Exception as e:
        print(f"爬取失败: {e}")

    return data

def crawl_weather2(url, name):
    weather_data = crawl_weather(url)
    df = pd.DataFrame(weather_data, columns=["城市", "天气", "最高温度", "最低温度"])
    df.to_csv(f"{name}.csv", index=False, encoding="utf-8-sig")
    print(f"爬取完成，数据已保存到 {name}.csv")
    print(df.head())
