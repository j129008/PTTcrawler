import json
import jieba
import jieba.analyse

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

with open('./data.json') as data_file:
    data = json.load(data_file)

for post in data:
    bad_push = post['h_推文總數']['b']
    KMTnum = 0
    KMTpush = ""
    if int(bad_push) < 10:
        continue
    for push in post['g_推文']:
        if "党工" in post['g_推文'][push]['留言內容']:
            KMTnum += 1
            KMTpush += post['g_推文'][push]['留言內容']+'\n'
    if KMTnum == 0:
        continue

    content = post['f_內文']
    tags = jieba.analyse.extract_tags(content)
    print(tags)
    print(KMTpush)
    print('==============================================')
