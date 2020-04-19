# 导入jieba库，jieba库是解决中文分词问题的常用第三方库
import jieba

# 打开准备好的出场人物名单
with open('names.txt') as f:
    nameList = f.read().split('\n')

# 打开三体三部曲全文
with open('three_body.txt') as f:
    txt = f.read()

# 向jieba库中加入人名，防止jieba在分词时将人名当作两个词拆分掉
for name in nameList:
    jieba.add_word(name)

# 分词
txt = jieba.lcut(txt)

# 遍历人物名单，计算人物出场次数
count = {}
for item in txt:
    for name in nameList:
        if item == name:
            count[name] = count.get(name, 0) + 1

# 排序并输出结果
count = sorted(count.items(), key=lambda kv: kv[1], reverse=True)
for item in count[:10]:
    print(item)