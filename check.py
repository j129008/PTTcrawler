from predict import predict

f = open('./pred_zh.json', 'r')
for ele in f:
    if predict(ele) >= 2:
        print(ele)
