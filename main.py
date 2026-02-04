import weather_crawler
import data_processor



url = "http://www.weather.com.cn/textFC/hb.shtml"
filename = input("请为爬取的文件命名:(已自动添加后缀.csv)")
print("开始爬取...")
weather_crawler.crawl_weather2(url, filename)

print("开始处理数据...")
data_processor.process_data(filename)