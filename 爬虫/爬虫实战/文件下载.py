import csv,requests
number = 0
with open('sharefile.csv','r',encoding = 'utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if number == 11:
            break
        res = requests.get(row['文档链接'])
        name = row['文档名字'] + '.pdf'
        res_data = res.content
        number += 1
        with open('爬虫下载的文档/'+ name,'wb') as f2:
            f2.write(res_data)