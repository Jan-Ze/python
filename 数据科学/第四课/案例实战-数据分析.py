import pandas as pd

mask_data_clean = pd.read_csv('课程素材/工作/mask_data_clean.csv')

mask_data_clean.groupby('月份')['销售额']