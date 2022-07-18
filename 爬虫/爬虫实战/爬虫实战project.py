import requests
# 功能1：通过搜索接口获取股票id数据
def search():
    while True:
        # 输入关键词
        keyword = input('请输入搜索关键词：')

        # 向搜索接口发起请求,获取数据
        params = {
            'keyWord': keyword,
            'maxNum': 10
        }
        r = requests.post('http://www.cninfo.com.cn/new/information/topSearch/query', params=params)

        # 过滤A股
        data = []
        for i in r.json():
            if i['category'] == 'A股':
                data.append(i)

        # 判断是否无搜索结果，如果无搜索结果就重新循环
        if len(data) == 0:
            print('无结果')
            continue
        # 将序号与股票绑定，方便后续取出股票信息
        result_dict = {}
        index = 1
        for row in data:
            result_dict[str(index)] = row

            # 顺便打印股票名称和对应序号
            print("【序号-{}】 名称 - {} 代码 - {} ".format(index, row['zwjc'], row['code']))
            index += 1

        print("序号：0 【我想重新输入关键词】\n")

        # 让用户选择序号
        while True:
            choice = input('请选择序号：')
            # 如果选择的序号存在股票字典里，则返回结果
            if choice in result_dict:
                return(result_dict[choice])
            # 如果是0则中止这个循环
            if choice == '0':
                break
            # 否则，打印提示
            else:
                print('输入了不存在的序号，请重新输入!')
print(search()) 