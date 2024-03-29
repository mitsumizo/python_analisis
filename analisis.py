import json
from janome.tokenizer import Tokenizer

import numpy as np
from scipy import stats

def main():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        json_dict = json.load(json_file)
        texts = []
        for json_key in json_dict:
            texts.append(json_key['detail'].replace('\n', ''))


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
    #
if __name__ == '__main__':
    main()
