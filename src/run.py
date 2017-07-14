# -*- coding: utf-8 -*-

"""
main
"""
__author__ = "Yuto Akagawa"
__date__    = "20170714"

import os
import os.path
import csv
import sys
import pandas as pd
from search import Search

def main(data_path):
    search = Search()
    data = pd.read_csv(data_path, header=None)
    result = []
    for i in range(len(data)): 
        keyword = data[0][i]
        print keyword
        result.append(search.google_search(keyword))
    print result
    result_df = pd.DataFrame(result)
    result_df.to_csv('../data/result.csv', index=False)    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "第一引数にデータファイルのパスを指定してください"
    main(sys.argv[1])

