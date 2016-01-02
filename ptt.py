import json
import jieba
import jieba.analyse

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

with open('./data.json') as data_file:
    data = json.load(data_file)

for post in data:
    content = post['f_內文']
    tags = jieba.analyse.extract_tags(content)
    print(tags)
