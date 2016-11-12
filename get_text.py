#!/usr/local/env python
# -*- encoding: utf-8 -*-

import json
import re

def filtering_osomatsu(text):
    r = re.compile(r"^@[^ ]+? ")
    # お知らせツイートは無視
    if u"話のセリフを追加しました" in text: return None
    # RTはおそ松のセリフじゃないので無視
    elif text[0:2] == u"RT": return None

    text = r.sub("", text)  # @を削除
    text = text.replace(u" ", u"")  # 空白を削除
    return text

def main():
    account = 'osomatsu_bot'
    infile = account + '.json'
    outfile = account + '.txt'

    ofh = open(outfile, 'w')
    for idx, tweets in json.load(open(infile, 'r')).items():
        for tweet in tweets:
            text = tweet['text']
            text = filtering_osomatsu(text)
            if not text: continue
            ofh.write( (text + u"\n").encode('utf-8') )
    ofh.close()

if __name__ == '__main__': main()
