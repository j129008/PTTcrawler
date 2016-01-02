import json
import jieba
import jieba.analyse

with open('./data.json') as data_file:
    data = json.load(data_file)

content = data[1]['f_內文']
tags = jieba.analyse.extract_tags(content)
print(tags)
