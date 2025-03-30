import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 模拟订单、物流和库存数据
order_data = {
    'order_id': [1, 2, 3],
    'order_date': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'order_amount': ['$100', '$200', '$300']
}
order_df = pd.DataFrame(order_data)

logistics_data = {
    'order_id': [1, 2, 3],
    'logistics_provider': [None, 'Provider A', 'Provider B']
}
logistics_df = pd.DataFrame(logistics_data)

inventory_data = {
    'order_id': [1, 2, 3],
    'inventory_quantity': [10, 20, 30]
}
inventory_df = pd.DataFrame(inventory_data)

# 多表合并
merged_df = pd.merge(order_df, logistics_df, on='order_id')
merged_df = pd.merge(merged_df, inventory_df, on='order_id')

# 日期格式化
merged_df['order_date'] = pd.to_datetime(merged_df['order_date'])

# 金额去符号化
merged_df['order_amount'] = merged_df['order_amount'].str.replace('$', '').astype(float)

# 空值填充
merged_df['logistics_provider'] = merged_df['logistics_provider'].fillna('未知')

# 可视化展示
# 订单金额分布直方图
plt.figure(figsize=(10, 6))
sns.histplot(merged_df['order_amount'], bins=10, kde=False)
plt.title('订单金额分布直方图')
plt.xlabel('订单金额')
plt.ylabel('数量')
plt.show()

# 物流商占比饼图
logistics_provider_counts = merged_df['logistics_provider'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(logistics_provider_counts, labels=logistics_provider_counts.index, autopct='%1.1f%%')
plt.title('物流商占比饼图')
plt.show()

# 数据导出
merged_df.to_csv('cleaned_data.csv', index=False)
merged_df.to_excel('cleaned_data.xlsx', index=False)