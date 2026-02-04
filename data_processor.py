import pandas as pd

# 从CSV文件读取数据
df = pd.read_csv("weather_data.csv", encoding="utf-8")

# 在温度列的数据转换为浮点数
df["最高温度"] = pd.to_numeric(df["最高温度"], errors="coerce").astype("float")
df["最低温度"] = pd.to_numeric(df["最低温度"], errors="coerce").astype("float")

# 添加平均气温列
df["平均气温"] = (df["最高温度"] + df["最低温度"]) / 2

# 添加温差列
df["温差"] = df["最高温度"] - df["最低温度"]

# 添加日期列
df["日期"] = None
time_list = ['星期三', '星期四', '星期五', '星期六', '星期日', '星期一', '星期二']
j=0
for i in range(0,482,69):
    df.loc[i:i+69, "日期"] = time_list[j]
    j += 1

# 将df转换为JSON文件
df.to_json("weather_data.json", force_ascii=False, orient="records")
