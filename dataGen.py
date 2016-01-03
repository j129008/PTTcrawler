import json
import jieba
import jieba.analyse
import operator

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

with open('./data.json') as data_file:
    data = json.load(data_file)

instance = {}
for post in data:
    instance['5F'] = 0
    instance['肥宅'] = 0
    instance['魯宅'] = 0
    instance['本魯'] = 0
    instance['小魯'] = 0
    instance['魯蛇'] = 0
    instance['女生'] = 0
    instance['分手'] = 0
    instance['正妹'] = 0
    instance['女朋友'] = 0
    instance['老婆'] = 0
    instance['女人'] = 0
    instance['女友'] = 0
    instance['妹妹'] = 0
    instance['馬習'] = 0
    instance['總統'] = 0
    instance['馬英九'] = 0
    instance['國民黨'] = 0
    instance['中國'] = 0
    instance['媒體'] = 0
    instance['記者'] = 0

    for push in post['g_推文']:
        if "五楼" in post['g_推文'][push]['留言內容']:
            instance['5F'] = 1

    content = post['f_內文']
    if "肥宅" in content:
        instance['肥宅'] = 1
