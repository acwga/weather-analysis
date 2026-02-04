import weather_crawler
import data_processor
import visualizer
import time



url = "http://www.weather.com.cn/textFC/hb.shtml" # 华北地区天气预报网址
filename = input("请为爬取的文件命名:(已自动添加后缀.csv)") # 文件名

# 开始爬取天气数据
print("开始爬取...")
weather_crawler.crawl_weather2(url, filename)

# 处理爬取的数据
print("开始处理数据...")
data_processor.process_data(filename)

# 读取处理后的数据
data_list = visualizer.read_file(filename)

# 生成柱状图
print("正在为您生成柱状图...")
time.sleep(2)
visualizer.draw_top10_bar(data_list)

# 生成饼图
print("正在为您生成饼图...")
time.sleep(2)
visualizer.draw_weather_pie(data_list)

# 生成地图
print("正在为您生成地图...")
time.sleep(2)
visualizer.draw_hebei_avg_temp_map(data_list)