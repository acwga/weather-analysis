import json
from pyecharts.charts import Bar, Timeline, Map, Pie
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取JSON文件
def read_file(name):
    f = open(f"{name}.json", "r", encoding="utf-8")
    data = f.read()
    f.close()

    # 将JSON字符串转换为Python列表
    data_list = json.loads(data) # 总数据列表
    return data_list

# 最高温度TOP10城市柱状图
def draw_top10_bar(data_list):
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
        # 添加数据
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
    timeline.render("未来七天华北地区最高温度TOP10城市.html")

# 华北地区未来七天天气分布饼图
def draw_weather_pie(data_list):
    weather_count = {}
    # 统计各类天气出现的次数
    for record in data_list:
        weather = record["天气"]
        try:
            weather_count[weather] += 1
        except KeyError:
            weather_count[weather] = 1
    # 将统计结果转换为元组并放入列表
    weather_data = []
    for w in weather_count.keys():
        weather_data.append((w, weather_count[w])) 
    # 构建饼图
    pie = Pie()
    # 添加数据
    pie.add("未来七天华北地区天气分布",weather_data, radius=["30%", "70%"], label_opts=LabelOpts(formatter="{b}, {d}%"))
    # 设置标题
    pie.set_global_opts(
        title_opts=TitleOpts(title="未来七天华北地区天气分布饼图")
    )
    # 绘图
    pie.render("未来七天华北地区天气分布饼图.html")

# 河北各城市平均温度分布地图
def draw_hebei_avg_temp_map(data_list):
    city_temp_list = []
    # 计算各城市的平均温度
    city_temp_sum = {} # 计算总温度
    city_temp_count = {} # 计算出现次数
    for record in data_list:
        if record["所在地区"] != "河北":
            continue
        city = record["城市"] + "市"
        temp = record["平均气温"]
        try:
            if temp is None:
                continue
            city_temp_sum[city] += temp
            city_temp_count[city] += 1
        except KeyError:
            if temp is None:
                continue
            city_temp_sum[city] = temp
            city_temp_count[city] = 1
    for city in city_temp_sum.keys():
        avg_temp = city_temp_sum[city] / city_temp_count[city]
        city_temp_list.append((city, round(avg_temp, 2)))
    # 构建地图
    map = Map()
    # 添加数据
    map.add("未来七天河北地区平均气温分布", city_temp_list, "河北")
    # 设置全局选项
    map.set_global_opts(
        title_opts=TitleOpts(title="未来七天河北地区平均气温分布地图"),
        visualmap_opts=VisualMapOpts(
            is_show=True, # 显示图例
            is_piecewise=True, # 分段显示
            pieces=[
                {"min": -20, "max": -11, "label": "-20~-10℃", "color": "#4B33FF"},
                {"min": -10, "max": -0, "label": "-10-0℃", "color": "#66B8FF"},
                {"min": 0, "max": 9, "label": "0-10℃", "color": "#66FFB3"},
                {"min": 10, "label": "10℃以上", "color": "#FFFF33"}
            ]
        )
    )
    # 绘图
    map.render("未来七天河北地区平均气温分布地图.html")