import numpy as np
from input_values import neighbors
import networkx as nx
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction import DictVectorizer
print(neighbors)
dict = neighbors

restructured = []

for key in dict:
    data_dict = {}
    for news in dict[key]:
        data_dict[news] = 1
    # data_dict['news3'] = 0
    restructured.append(data_dict)

# restructured should now look like
'''
[{'news1':1, 'news2':1, 'news3':0},
 {'news2':1, 'news4':1, 'news3':0},
 {'news1':1, 'news4':1, 'news3':0}]
'''

dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(restructured)

print(features)

# output
'''
[[1, 1, 0, 0],
 [0, 1, 1, 0],
 [1, 0, 1, 0]]
'''
print(dictvectorizer.get_feature_names())
# output
