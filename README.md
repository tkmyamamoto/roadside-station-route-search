<div align="center">
  <img src="resources/logo_repository.png" width="600"/>
</div>

道の駅のルート検索を行う．

## Prerequirements

- Python 3.7
- CUDA 11.3

## Setup

```sh
$ cd setup_venv

# check version setting
$ make showenv
==================================================
- PYTHON_VERSION=3.7
- PYTORCH_VERSION=1.12.1
- TORCH_VISION_VERSION=0.13.1
- CUDA_VERSION=11.3
==================================================

# make
$ make

# activate created virtualenv
$ . rsrs_env/bin/activate
```

## Data Preparation

データは[ここ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P35.html)からダウンロードする．

解凍した`P35-18_GML`フォルダは以下の通りに配置する．
```sh
.
├── data
│   └── P35-18_GML
├── rsrs
├── pyproject.toml
├── README.md
└── setup_venv
```

### 地域の定義

- 北海道地方  
国土交通省北海道開発局管内（北海道）
- 東北地方  
国土交通省東北地方整備局管内（青森県、秋田県、岩手県、山形県、福島県、宮城県）
- 関東地方  
国土交通省関東地方整備局管内（茨城県、栃木県、群馬県、埼玉県、千葉県、東京都、神奈川県、山梨県、長野県北部・中部）
- 中部地方  
国土交通省中部地方整備局管内（長野県南部、岐阜県、静岡県、愛知県、三重県）
- 北陸地方  
国土交通省北陸地方整備局管内（新潟県、富山県、石川県）
- 近畿地方  
国土交通省近畿地方整備局管内（福井県、滋賀県、京都府、大阪府、兵庫県、奈良県、和歌山県）
- 中国地方  
国土交通省中国地方整備局管内（鳥取県、島根県、岡山県、広島県、山口県）
- 四国地方  
国土交通省四国地方整備局管内（徳島県、高知県、愛媛県、香川県）
- 九州地方  
国土交通省九州地方整備局管内（福岡県、佐賀県、長崎県、熊本県、大分県、宮崎県、鹿児島県）
内閣府沖縄総合事務局管内（沖縄県）

#### 長野県の10区分け
<details><summary>Expand Details</summary><div>
参考：https://www.pref.nagano.lg.jp/10koiki/index.html

- 長野県北部  
北アルプス，長野，北信
- 長野県中部  
佐久，上田，諏訪，松本
- 長野県南部  
上伊那，南信州，木曽

![長野県の10区分け](https://www.pref.nagano.lg.jp/10koiki/images/10kouiki.jpg)
</div></details>

#### 都道府県コード

<details><summary>Expand Code List</summary><div>

| 当道府県名 | コード |
|:-----------|------------:|
|北海道|1|
|青森県|2|
|岩手県|3|
|宮城県|4|
|秋田県|5|
|山形県|6|
|福島県|7|
|茨城県|8|
|栃木県|9|
|群馬県|10|
|埼玉県|11|
|千葉県|12|
|東京都|13|
|神奈川県|14|
|新潟県|15|
|富山県|16|
|石川県|17|
|福井県|18|
|山梨県|19|
|長野県|20|
|岐阜県|21|
|静岡県|22|
|愛知県|23|
|三重県|24|
|滋賀県|25|
|京都府|26|
|大阪府|27|
|兵庫県|28|
|奈良県|29|
|和歌山県|30|
|鳥取県|31|
|島根県|32|
|岡山県|33|
|広島県|34|
|山口県|35|
|徳島県|36|
|香川県|37|
|愛媛県|38|
|高知県|39|
|福岡県|40|
|佐賀県|41|
|長崎県|42|
|熊本県|43|
|大分県|44|
|宮崎県|45|
|鹿児島県|46|
|沖縄県|47|

</div></details>

#### 地域コード

<details><summary>Expand Code List</summary><div>

| 地域名 | コード |
|:-----------|------------:|
|北海道地方|1|
|東北地方|2|
|関東地方|3|
|中部地方|4|
|北陸地方|5|
|近畿地方|6|
|中国地方|7|
|四国地方|8|
|九州地方|9|

</div></details>

## Run Scripts

### Preparation

- `PYTHONPATH`を通す．
```sh
cd roadside-station-route-search

export PYTHONPATH="`pwd`/rsrs:"$PYTHONPATH
```

- rsrs_envをアクティベートする．
```sh
. setup_venv/rsrs_env/bin/activate
```

- 実行する．
```sh
# htmlに保存してから地図を見る
python tools/view_spots_html.py

# streamlitで地図を見る
streamlit run tools/view_spots_streamlit.py
```
