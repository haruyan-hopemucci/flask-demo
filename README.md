# 作業

## 環境の準備

### venvで仮想環境設定（必須ではない）

```cmd
> pip install venv
> python -m venv venv
> .\venv\Scripts\activate
```

※PowerShellでactivateを実行するには、スクリプトファイル実行許可を予め指定しなければならない。

```
c:\work>PowerShell Set-ExecutionPolicy RemoteSigned
```

実行には管理者権限が必要。

それが不可能な場合は、コマンドプロンプトで同様にactivateを実行する。

### flaskのインストール

`pip install flask`

## チュートリアル

flask公式のチュートリアルは「超シンプルなものから段階的に」という感じではないので、qiitaから検索してきたどシンプルなページの作成を参考にする。

https://qiita.com/kiyokiyo_kzsby/items/0184973e9de0ea9011ed

とりあえずDay3まで消化できればチュートリアルとしてはOKだと思う。
Day4以降はデータベース操作だったりログイン機能だったりを実装するが、このようにデータベース操作を伴うような実装はもはやflaskではなくDjangoを使った方が良い。
（Djangoでは記事のような複雑なことをしなくてもデフォルトでDB操作やログイン機能がついている）
flaskはあくまで「マイクロフレームワーク」で最小限のWebページをpythonで実現するために作成されているので、あまりゴテゴテした機能を実装するのであれば他のフレームワークの使い方を覚えたほうが良い。

## covid-19 APIサイト

https://corona.go.jp/dashboard/

リアルタイム集計ではなく、数日前の情報しか見ることができないようなので、3日前の情報限定で取得するようにする。
また、「当日の感染者数」は提供されず、総感染者数のみ（都道府県別）なので、当日から前日の総感染者数を引き算して計算している。