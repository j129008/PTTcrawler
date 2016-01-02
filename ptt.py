import json
import jieba
import jieba.analyse

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

with open('./data.json') as data_file:
    data = json.load(data_file)

content = data[1]['f_內文']
tags = jieba.analyse.extract_tags(content)
print(tags)
