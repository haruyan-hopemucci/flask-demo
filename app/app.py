#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
import datetime
import urllib.request
import json

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
  return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
  # 情報サイトからcovid-19の総感染者数を取得する
  dt = datetime.date.today()
  # 本日の情報は無いみたい。3日前くらいならあるかな？
  dt = dt + datetime.timedelta(days=-3)
  dt_str = dt.strftime("%Y%m%d")  # 2022-01-19 => 20220119
  dt_str_html = dt.strftime("%Y年%m月%d日")
  url = f"https://opendata.corona.go.jp/api/Covid19JapanAll?date={dt_str}"
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as res:
      body = json.load(res)
  total = 0
  for item in body['itemList']:
    total = total + int(item['npatients'])
  total_today = total

  # 前日の感染者
  dt = dt + datetime.timedelta(days=-1)
  dt_str = dt.strftime("%Y%m%d")  # 2022-01-19 => 20220119
  url = f"https://opendata.corona.go.jp/api/Covid19JapanAll?date={dt_str}"
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as res:
      body = json.load(res)
  total = 0
  for item in body['itemList']:
    total = total + int(item['npatients'])
  total_yestarday = total

  # 当日の感染者数
  iop = total_today - total_yestarday
  return render_template("index.html", dt_str=dt_str_html, infected_people=iop)


#おまじない
if __name__ == "__main__":
  app.run(debug=True)