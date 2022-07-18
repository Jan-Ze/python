import pandas as pd
# 创建两个原始列表
new_df = pd.DataFrame({'年龄':[1,2,3,4],
                      '性别':["男","男","男","男"]})

print(new_df['年龄'][0])