import requests

# 功能一
def search():
    while True:
        keyword = input('请输入搜索关键词：')
        params = {
            'keyWord':keyword,
            'maxNum': 10
        }
        r = requests.post('http://www.cninfo.com.cn/new/information/topSearch/query',params = params)
        data = []
        for i in r.json():
            if i['category'] == 'A股':
                data.append(i)
        if len(data) == 0:
            print('无搜索结果，请重新输入')
            continue
        result_dict = {}
        index = 1
        for row in data:
            result_dict[str(index)] = row
            print("【序号-{}】 名称 - {} 代码 - {} ".format(index, row['zwjc'], row['code']))
            index += 1
        print("序号：0 【我想重新输入关键词】\n")
        while True:
            choice = input('请选择序号：')
            if choice in result_dict:
                return (result_dict[choice]['code'],result_dict[choice]['orgId'])
            if choice == '0':
                break
            else:
                print('不存在此序号，请重新输入')
                
# 功能二
def select(code,orgid):
    while True:
        category_dict = {
            "1": "category_ndbg_szsh;",
            "2": "category_bndbg_szsh;",
            "3": "category_rcjy_szsh;"
        }
        numbers = (input('请输入搜索类型序号：1、年报 2、半年报 3、日常经营：（输入序号，如：1）'))
        if numbers != '1' and numbers != '2' and numbers != '3':
            print('未选择任何搜索类型或者不存在此类型，请重新选择\n')
            continue
        else:
            category = category_dict[numbers]
            break
    start = input('请输入搜索范围起始时间(例如 2021-01-01)：')
    end = input('请输入搜索范围结束时间(例如 2021-07-01)：')
    if code[0] == '6':
        column = 'sse'
        plate = 'sh'
    else:
        column = 'szse'
        plate = 'sz'
    page_num = 1
    pdf_list = []
    while True:
        
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
        r = requests.post('http://www.cninfo.com.cn/new/hisAnnouncement/query', data=data)
        r_json = r.json()
        if r_json['announcements'] == None:
            print('文档一共有{}页'.format(str(page_num-1)))
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
# 功能三
def download(pdf_list):
    num = 1
    for item in pdf_list:
        url = 'http://static.cninfo.com.cn/' + item[1]
        name = item[0] + '.pdf'
        with open(name,'wb') as f:
            f.write(requests.get(url).content)
            print('下载成功{}个文件'.format(num))
            num = num+1
# 功能整合
def main():
    code,orgid = search()
    pdf_list = select(code,orgid)
    download(pdf_list)
    # 搜索股票，获取股票id信息等

    # 输入各个参数，筛选报告
main()

    # 下载报告