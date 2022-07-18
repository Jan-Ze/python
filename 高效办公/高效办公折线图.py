import os
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference, BarChart

# 设置目标文件夹路径
path = './各部门利润表汇总/'
# 获取文件夹下的所有文件名
file_list = os.listdir(path)
# 遍历文件名列表，取得每一个文件名
for file_name in file_list:
    # 拼接文件路径
    file_path = path + file_name
    print('正在处理：' + file_name)
    # 读取工作簿
    wb = load_workbook(file_path)
    # 定位到工作簿中的活跃工作表
    ws = wb.active

    # 实例化 LineChart() 类，得到 LineChart 对象
    chart = BarChart()
    # 引用工作表的部分数据
    data = Reference(worksheet = ws, min_row=3, max_row=9, min_col=1, max_col=5)
    # 添加被引用的数据到 LineChart 对象
    chart.add_data(data, from_rows=True, titles_from_data=True)
    # 添加 LineChart 对象到工作表中，指定生成折线图的位置
    ws.add_chart(chart, "C12")

    # 引用工作表的表头数据
    cats = Reference(worksheet=ws, min_row=2, max_row=2, min_col=2, max_col=5)
    # 设置类别轴的标签
    chart.set_categories(cats)
    # 设置 x 轴的标题
    chart.x_axis.title = "季度"
    # 设置 y 轴的标题
    chart.y_axis.title = "利润"
    # 设置折线图的颜色
    chart.style = 48

    # 保存工作簿
    wb.save(file_path)