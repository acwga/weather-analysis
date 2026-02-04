import json
from pyecharts.charts import Bar, Timeline, Map
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取JSON文件
f = open("weather_data.json", "r", encoding="utf-8")
data = f.read()
f.close()

# 将JSON字符串转换为Python列表
data_list = json.loads(data) # 总数据列表

# 最高温度TOP10城市柱状图
data_dict = {}
for record in data_list:
    date = record["日期"]
    city = record["城市"]
    high_temp = record["最高温度"]
    try:
        data_dict[date].append([city, high_temp]) # 添加[城市和最高温度]到字典为value, 日期date为key
    except KeyError:
        data_dict[date] = []
        data_dict[date].append([city, high_temp])
# 构建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)
# 取出温度前10的城市
for d in data_dict.keys():
    data_dict[d].sort(key=lambda element: element[1] if element[1] is not None else -1e9, reverse=True)
    date_data = data_dict[d][0:10]
    date_data.reverse() # 反转列表, 使得温度最高的城市在最上方
    x_data = []
    y_data = []
    for city_temp in date_data:
        x_data.append(city_temp[0]) # 城市
        y_data.append(city_temp[1]) # 最高温度
    # 构建柱状图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("最高温度(℃)", y_data, label_opts=LabelOpts(position="right"), bar_min_height=20)
    bar.reversal_axis() # 反转坐标轴
    # 设置标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{d}全国最高温度TOP10城市")
    )
    timeline.add(bar, str(d))

# 时间线自动播放
timeline.add_schema(
    play_interval=1000, # 播放间隔 : 1秒
    is_timeline_show=True, # 显示时间线
    is_auto_play=True, # 自动播放
    is_loop_play=False # 不循环播放
)
# 绘图
timeline.render("未来七天全国最高温度TOP10城市.html")

# 温度分布地图

# 天气分布地图