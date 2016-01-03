import json
import jieba
import jieba.analyse
# import operator

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

with open('./data.json') as data_file:
    data = json.load(data_file)

instance = {}
genData = []
for post in data:
    instance['5F'] = 0
    instance['loser'] = 0
    instance['loser_self'] = 0
    instance['girl'] = 0
    instance['beauty'] = 0
    instance['sister'] = 0
    instance['taiwan'] = 0
    instance['reporter'] = 0
    instance['news'] = 0

    for push in post['g_推文']:
        if "五楼" in post['g_推文'][push]['留言內容']:
            instance['5F'] = 1

    content = post['f_內文']
    if "鲁蛇" in content:
        instance['loser'] = 1
    if "鲁宅" in content:
        instance['loser'] = 1
    if "肥宅" in content:
        instance['loser'] = 1

    if "本鲁" in content:
        instance['loser_self'] = 1
    if "小鲁" in content:
        instance['loser_self'] = 1

    if "女生" in content:
        instance['girl'] = 1
    if "分手" in content:
        instance['girl'] = 1
    if "老婆" in content:
        instance['girl'] = 1
    if "女人" in content:
        instance['girl'] = 1
    if "女友" in content:
        instance['girl'] = 1
    if "妹妹" in content:
        instance['sister'] = 1
    if "正妹" in content:
        instance['beauty'] = 1
    if "马习"  in content:
        instance['taiwan'] = 1
    if  "总统" in content:
        instance['taiwan'] = 1
    if  "马英九"  in content:
        instance['taiwan'] = 1
    if  "国民党" in content:
        instance['taiwan'] = 1
    if  "中国" in content:
        instance['taiwan'] = 1
    if "媒体" in content:
        instance['news'] = 1
    if "记者" in content:
        instance['reporter'] = 1
    # genData.extend(instance)
    print(instance)

