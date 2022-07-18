import csv
file = "books.csv"

head = ['作者','出版社','ISBN','页数','出版年','定价']
'''
dict1 = {'name':'Ze','score':100}
dict2 = {'name':'dad','score':80}
with open(file,'w',encoding = 'utf-8') as f:
    writer = csv.DictWriter(f,fieldnames = head)
    writer.writeheader()
    writer.writerows([dict1,dict2])

'''
rows = []
with open(file,'r',encoding = 'utf-8') as f:
    reader = csv.DictReader(f)
    head = reader.fieldnames
    print(head)
    for row in reader:
        rows.append(row)



    
    