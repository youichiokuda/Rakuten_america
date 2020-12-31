# Rakuten_america

楽天の全米型インデックスファンドがいいよ。ということなので（By じっちゃま。https://twitter.com/hirosetakao　）FacebookのProphetで分析と予測をしてみました。


最初にpipでインストール。

$ pip install fbprophet

CSVはここからダウンロード。

https://www.morningstar.co.jp/FundData/Download.do?fnc=2017092908

'rakutenindex.csv'という名前でローカルにおいて分析しています。

日付がintなのでstrに変えて、Prophetはdsとyというカラムが必要なので日付をds価格をyにしています。

分析して感じたこと。

・まだ2020年12月30日現在で791日の歴史の浅いファンドだということ。

・コロナのパンデミックの影響で2020年3月に大幅に下落しており、それがモデルに与える影響が大きいこと。

・なぜか金曜に上がる傾向あり。なぜ？
