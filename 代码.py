import pandas as pd
import matplotlib.pyplot as plt

# 加载数据（需修改为你本地的路径）
df = pd.read_csv("F:\项目、数据集\diabetes\diabetes.csv")  

# 检查类别分布（核心缺陷点）
print("糖尿病阳性比例：", df['Outcome'].mean().round(2))  

# 检查缺失值（隐藏陷阱）
print("葡萄糖缺失情况：", (df['Glucose'] == 0).sum())  

# 生成可视化报告  
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
df['Outcome'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Class Distribution')

plt.subplot(1,2,2)
df['Insulin'].plot.hist(bins=20)
plt.title('Insulin Distribution')
plt.savefig('data_issues.png')  # 保存图片用于GitHub展示