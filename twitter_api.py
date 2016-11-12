#!/usr/local/env python
# -*- encoding: utf-8 -*-

api_key="ENTER YOUR API KEY"
api_secret="ENTER YOUR API SECRET"
access_token = "ENTER YOUR ACCESS TOKEN"
access_secret = "ENTER YOUR ACCESS SECRET"

import time
import json
from requests_oauthlib import OAuth1Session

# Tweetデータを取得する
def getTweetData(session, name, count, max_id=None, since_id=None):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {"screen_name": name,
             "count": count}

    if max_id: params['max_id'] = max_id
    if since_id: params['since_id'] = since_id
    req = session.get(url, params = params)

    # 取得データの読み込み
    timeline = json.loads(req.text)
    return timeline

# 何回かに分けてTweetデータを取得し、json形式で保存する
def main():
    max_id = None
    get_num = 100             # 一回に取得する件数 (100件ずつ取得)
    max_try = float("inf")    # 最大取得回数 (制限なし)
    sleep = 5                 # 待機時間
    account = "osomatsu_bot"  # 取得対象アカウント

    # OAuth1Sessionを作成
    session = OAuth1Session(api_key, api_secret, access_token, access_secret)

    # 出力ファイルをオープン
    ofh = open(account + ".json", "w")

    ofh.write("{\n")
    try_cnt = 1

    # 取得Tweetがなくなるまで繰り返す
    while True:
        ret = getTweetData(session, account, get_num, max_id=max_id)
        if not ret or len(ret) == 0: break

        if try_cnt > 1: ofh.write(",\n")
        ofh.write("\"%04d\": " % try_cnt)
        ofh.write(json.dumps(ret, indent=4))

        max_id = ret[-1]["id"] - 1  # 次の取得の開始idを指定
        try_cnt += 1
        if try_cnt > max_try: break  # try_cntが最大取得回数を超えたらbreak

        time.sleep(sleep)

    ofh.write("\n}")
    ofh.close()

if __name__ == "__main__": main()
