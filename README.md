# Tweet取得ツール

特定のアカウントのTweetをごそっと取得してくるツールです。
デフォルトでは@osomatsu\_botのTweetを取得します

# 検証環境
Mac OS X 10.11.6
python 2.7.11

# 使い方
## 前準備
### oauthlibのインストール
```
pip install requests_oauthlib
```
### Twitterのapi_key, api_secret, access_token, access_secretの取得
[このあたり](https://syncer.jp/twitter-api-matome)を参考に。

## Tweet取得
```
python twitter_api.py
```
同じフォルダに[アカウント名].jsonというファイルができます。
アカウントの変更はtwitter\_api.pyの39行目を編集してください。

取得したデータは以下のように保存されます。
(例) 1回の取得で100件ずつ、10回取得しに行った場合
```
{
 "0001": [
   { ツイートデータ1 }, { ツイートデータ2 }, ...
 ],
 "0002": [
   { ツイートデータ101 }, { ツイートデータ102 }, ...
 ],

 ...

 "0010" : [
   { ツイートデータ901 }, { ツイートデータ902 }, ...
 ]
}
```

## テキスト部分を抽出
```
python get_text.py
```
アカウントの変更はget_text.pyの19行目を編集してください

## 重複しているテキストをuniq(オプション)
```
cat osomatsu_bot.txt | sort | uniq > uniq_osomatsu_bot.txt
```
