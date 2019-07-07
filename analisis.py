import json
from janome.charfilter import *
from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import *

import numpy as np
from scipy import stats

json_file = open('data.json', 'r', encoding='utf-8')
json_dict = json.load(json_file)
texts = []
for json_key in json_dict:
    texts.append(json_key['detail'].replace('\n', ''))

json_file.close()

t = Tokenizer()

result = list()
all = 0
for rank in range(len(texts)):
    kind = []
    text = t.tokenize(texts[rank],wakati=True)
    type = 0
    for word in text:
        if not word in kind:
            kind.append(word)
            type += 1
            all += 1
    result.append({'rank': rank + 1, 'type': type})

# print('all: ' + str(all))
# print('average: ' + str(all / len(texts)))

first = np.empty(50)
second = np.empty(50)

for rank in range(50):
    first[rank:rank+1] = result[rank]['type']

for index in range(50):
    second[index:index+1] = result[index + 50]['type']

# print(first)
# print(second)
print(stats.ttest_ind(first, second))
#Ttest_indResult(statistic=0.23367427377675823, pvalue=0.8157252926627823)
# -> 有意義とはいえない。
