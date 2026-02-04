import pandas as pd

# 查看最小最低和最大最高气温
df = pd.read_csv("weather_data.csv", encoding="utf-8")
print("最低气温最小值:", df["最低温度"].min())
print("最高气温最大值:", df["最高温度"].max())