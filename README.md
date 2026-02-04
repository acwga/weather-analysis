# 中国华北地区天气数据分析与可视化项目

## 项目简介

使用Python从中国天气网爬取华北地区城市天气数据，进行清洗、统计分析，并用pyecharts绘制柱状图、饼图和热力地图，展示不同城市之间的温度差异以及天气类型占比。

## 技术栈

- Python 3.10.19
- requests + BeautifulSoup (网页爬取)
- pandas （数据处理）
- pyecharts （交互式图表可视化）
- Python标准库：time、json、random

## 运行步骤

1. 安装依赖
2. 运行主程序： python main.py
3. 输入文件名（自动保存为.csv）
4. 查看生成的HTML图表文件

## 项目成果

- 爬取数据：华北地区城市的天气信息
- 统计分析：平均温度，温差，城市所属省/直辖市等
- 可视化示例：
- `高温度TOP10城市柱状图`
- `华北地区未来七天天气分布饼图`
- `河北各城市平均温度分布地图`
<img width="1404" height="826" alt="屏幕截图 2026-02-04 185825" src="https://github.com/user-attachments/assets/6ab6c65a-fc8f-4222-91b0-b2e69aa9c74c" />
<img width="1367" height="707" alt="image" src="https://github.com/user-attachments/assets/c809b264-00c6-4ea4-8d7c-cb438ddac3aa" />
<img width="1091" height="779" alt="image" src="https://github.com/user-attachments/assets/d6b937a6-62bf-46a2-9a83-0354e54b4586" />
