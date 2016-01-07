import json
import jieba
import jieba.analyse
import operator

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

with open('./data.json') as data_file:
    data = json.load(data_file)

allTag = []
cnt = 0
for post in data:
    bad_push = post['h_推文總數']['b']
    KMTnum = 0
    KMTpush = ""
    for push in post['g_推文']:
        if ("五楼" or "5F" or "5f" ) in post['g_推文'][push]['留言內容']:
            KMTnum += 1
            KMTpush += post['g_推文'][push]['留言內容']+'\n'
    if KMTnum == 0:
        continue

    content = post['f_內文']
    tags = jieba.analyse.extract_tags(content,topK=3)
    allTag = allTag + tags
    # print(tags)
    # print(KMTpush)
    # print('==============================================')
    cnt += 1

d = {}
for ele in allTag:
    try:
        d[ele] += 1
    except:
        d[ele] = 1
d = sorted(d.items(), key=operator.itemgetter(1))
for ele in d:
    print(ele[0])
# print(cnt)
