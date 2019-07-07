import json
from janome.charfilter import *
from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import *

json_file = open('data.json', 'r', encoding='utf-8')
json_dict = json.load(json_file)
texts = []
for json_key in json_dict:
    texts.append(json_key['detail'].replace('\n', ''))

json_file.close()

t = Tokenizer()

result = list()
for rank in range(len(texts)):
    kind = []
    text = t.tokenize(texts[rank],wakati=True)
    type = 0
    for word in text:
        if not word in kind:
            kind.append(word)
            type += 1
    result.append({'rank': rank + 1, 'type': type})

for re in result:
    print(re)


# texts = '僕は疲れました。僕は教育を変えたいです。'
# t = Tokenizer()
#
# text = t.tokenize(texts, wakati=True)
#
# kind = []
# type = 0
# for word in text:
#     if not word in kind:
#         kind.append(word)
#         type += 1
#
# print(kind)
# print(type)
