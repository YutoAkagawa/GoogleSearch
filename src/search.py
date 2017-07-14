# -*- coding: utf-8 -*-

"""
Google検索を行う
"""
__author__ = "Yuto Akagawa"
__date__    = "20170714"
import sys
from google import search

class Search:
    def init(self):
        pass

    def google_search(self, query, limit=1):
        num = 0
        urls = [query]
        for url in search(query, lang="en", num=limit, pause=2.0):
            if num > 9:
                break
            print "検索結果=>", num
            print url
            url_parse = url.split("//")[1].split("/")[0]
            print url_parse
            urls.append(url_parse)
            num += 1
            print urls
        return urls

if __name__ == '__main__':
    s = Search()
    print s.google_search("qiita")

