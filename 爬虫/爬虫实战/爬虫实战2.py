import requests
import csv
head = ['文档名字','文档链接']
www = []
code = '601012'
orgid = '9900022338'

# 功能2：筛选报告

def select(code, orgid):
    while True:

    # 获取报告类型

        # 初始化一个类型字典
        category_dict = {
            "1": "category_ndbg_szsh;",
            "2": "category_bndbg_szsh;",
            "3": "category_rcjy_szsh;"
        }

        # 让用户选择需要下载的报告类型
        numbers = (input('请输入搜索类型序号：1、年报 2、半年报 3、日常经营：（输入序号，如：1）'))
        
        # 判断用户选择的类型是否存在，如果存在，则返回类型
        if numbers != '1' and numbers != '2' and numbers != '3':
            print('未选择任何搜索类型或者不存在此类型，请重新选择\n')
        # 否则，打印提示
        else:
            category = category_dict[numbers]
            break


    # 获取时间
    start = input('请输入搜索范围起始时间(例如 2021-01-01)：')
    end = input('请输入搜索范围结束时间(例如 2021-07-01)：')

    # 根据股票代码的头文字，判断股票交易所信息
    if code[0] == '6':
        column = 'sse'
        plate = 'sh'
    else:
        column = 'szse'
        plate = 'sz'

    # 筛选报告
    # 设置初始页码
    page_num = 1
    pdf_list = []
    while True:
        # 设置初始列表存储筛选结果

        # 设置报告筛选参数
        data = {
            'stock': '{},{}'.format(code, orgid),
            'tabName': 'fulltext',
            'pageSize': '30',
            'pageNum': str(page_num),
            'category': category,
            'seDate': '{}~{}'.format(start, end),
            'column': column,
            'plate': plate,
            'searchkey': '',
            'secid': '',
            'sortName': '',
            'sortType': '',
            'isHLtitle': ''
        }

        # 发起报告搜索请求
        r = requests.post('http://www.cninfo.com.cn/new/hisAnnouncement/query', data=data)
        # 解析相应数据
        r_json = r.json()
        # 判断是否搜索失败、或者无搜索结果，如果无结果则结束
        if r_json['announcements'] == None:
            print('第{}页已经没有任何文档'.format(str(page_num)))
            break
        # 遍历搜索结果，将筛选后的报告标题以及 url 以列表的形式嵌套至初识列表中
        for i in r_json['announcements']:
            pdf_list.append([i['announcementTitle'], i['adjunctUrl']])
        # 判断是否还有下一页数据，没有的话就结束循环
        if r_json['hasMore'] == 'false':
            break
        # 让页数加一，开始下一轮循环
        else:
            page_num += 1
        
    return pdf_list

pdf_list = select(code,orgid)
for i in pdf_list:
        mid = {}
        mid['文档名字'] = i[0]
        mid['文档链接'] = 'http://static.cninfo.com.cn/' + i[1]
        www.append(mid)
with open('sharefile.csv','wb',encoding = 'utf-8') as f:
    writer = csv.DictWriter(f,fieldnames = head)
    writer.writeheader()
    writer.writerows(www)
