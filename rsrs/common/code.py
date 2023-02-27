#!/usr/bin/env python
# coding: utf-8

PREFECTURES_JP_CODE = {
    "北海道": 1,
    "青森県": 2,
    "岩手県": 3,
    "宮城県": 4,
    "秋田県": 5,
    "山形県": 6,
    "福島県": 7,
    "茨城県": 8,
    "栃木県": 9,
    "群馬県": 10,
    "埼玉県": 11,
    "千葉県": 12,
    "東京都": 13,
    "神奈川県": 14,
    "新潟県": 15,
    "富山県": 16,
    "石川県": 17,
    "福井県": 18,
    "山梨県": 19,
    "長野県": 20,
    "岐阜県": 21,
    "静岡県": 22,
    "愛知県": 23,
    "三重県": 24,
    "滋賀県": 25,
    "京都府": 26,
    "大阪府": 27,
    "兵庫県": 28,
    "奈良県": 29,
    "和歌山県": 30,
    "鳥取県": 31,
    "島根県": 32,
    "岡山県": 33,
    "広島県": 34,
    "山口県": 35,
    "徳島県": 36,
    "香川県": 37,
    "愛媛県": 38,
    "高知県": 39,
    "福岡県": 40,
    "佐賀県": 41,
    "長崎県": 42,
    "熊本県": 43,
    "大分県": 44,
    "宮崎県": 45,
    "鹿児島県": 46,
    "沖縄県": 47,
}

PREFECTURES_EN_CODE = {
    "Hokkaido": 1,
    "Aomori": 2,
    "Iwate": 3,
    "Miyagi": 4,
    "Akita": 5,
    "Yamagata": 6,
    "Fukushima": 7,
    "Ibaraki": 8,
    "Tochigi": 9,
    "Gumma": 10,
    "Saitama": 11,
    "Chiba": 12,
    "Tokyo": 13,
    "Kanagawa": 14,
    "Niigata": 15,
    "Toyama": 16,
    "Ishikawa": 17,
    "Fukui": 18,
    "Yamanashi": 19,
    "Nagano": 20,
    "Gifu": 21,
    "Shizuoka": 22,
    "Aichi": 23,
    "Mie": 24,
    "Shiga": 25,
    "Kyoto": 26,
    "Osaka": 27,
    "Hyogo": 28,
    "Nara": 29,
    "Wakayama": 30,
    "Tottori": 31,
    "Shimane": 32,
    "Okayama": 33,
    "Hiroshima": 34,
    "Yamaguchi": 35,
    "Tokushima": 36,
    "Kagawa": 37,
    "Ehime": 38,
    "Kochi": 39,
    "Fukuoka": 40,
    "Saga": 41,
    "Nagasaki": 42,
    "Kumamoto": 43,
    "Oita": 44,
    "Miyazaki": 45,
    "Kagoshima": 46,
    "Okinawa": 47,
}

REGION_JP_CODE = {
    "北海道地方": 1,
    "東北地方": 2,
    "関東地方": 3,
    "中部地方": 4,
    "北陸地方": 5,
    "近畿地方": 6,
    "中国地方": 7,
    "四国地方": 8,
    "九州地方": 9,
}

REGION_JP_CONTENTS = {
    "北海道地方": ["北海道"],
    "東北地方": ["青森県", "秋田県", "岩手県", "山形県", "福島県", "宮城県"],
    "関東地方": ["茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "山梨県", "長野県北部", "長野県中部"],
    "中部地方": ["長野県南部", "岐阜県", "静岡県", "愛知県", "三重県"],
    "北陸地方": ["新潟県", "富山県", "石川県"],
    "近畿地方": ["福井県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県"],
    "中国地方": ["鳥取県", "島根県", "岡山県", "広島県", "山口県"],
    "四国地方": ["徳島県", "高知県", "愛媛県", "香川県"],
    "九州地方": ["福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県"],
}

NAGANO_SPLIT_10 = {
    # NOTE(tkmyamamoto): Refer to https://www.jma.go.jp/jma/kishou/know/saibun/nagano.pdf
    # NOTE(tkmyamamoto): Refer to https://www.pref.nagano.lg.jp/10koiki/index.html
    "北アルプス": ["大町市", "北安曇郡池田町", "松川村", "白馬村", "小谷村"],
    "長野": ["長野市", "須坂市", "千曲市", "埴科郡坂城町", "上高井郡小布施町", "高山村", "上水内郡信濃町", "小川村", "飯綱町"],
    "北信": ["中野市", "飯山市", "下高井郡山ノ内町", "木島平村", "野沢温泉村", "下水内郡栄村"],
    "佐久": [
        "小諸市",
        "佐久市",
        "南佐久郡小海町",
        "川上村",
        "南牧村",
        "南相木村",
        "北相木村",
        "佐久穂町",
        "北佐久郡軽井沢町",
        "御代田町",
        "立科町",
    ],
    "上田": ["上田市", "東御市", "小県郡青木村", "長和町"],
    "諏訪": ["岡谷市", "諏訪市", "茅野市", "諏訪郡下諏訪町", "富士見町", "原村"],
    "松本": ["松本市", "塩尻市", "安曇野市", "東筑摩郡麻績村", "生坂村", "山形村", "朝日村", "筑北村"],
    "上伊那": ["伊那市", "駒ヶ根市", "上伊那郡辰野町", "箕輪町", "飯島町", "南箕輪村", "中川村", "宮田村"],
    "南信州": [
        "飯田市",
        "下伊那郡松川町",
        "高森町",
        "阿南町",
        "阿智村",
        "平谷村",
        "根羽村",
        "下條村",
        "売木村",
        "天龍村",
        "泰阜村",
        "喬木村",
        "豊丘村",
        "大鹿村",
    ],
    "木曽": ["木曽郡上松町", "南木曽町", "木祖村", "王滝村", "大桑村", "木曽町"],
}

NAGANO_SPLIT_3 = {
    # NOTE(tkmyamamoto): Refer to https://www.jma.go.jp/jma/kishou/know/saibun/nagano.pdf
    # NOTE(tkmyamamoto): Refer to https://www.pref.nagano.lg.jp/10koiki/index.html
    "長野県北部": ["北アルプス", "長野", "北信"],
    "長野県中部": ["佐久", "上田", "諏訪", "松本"],
    "長野県南部": ["上伊那", "南信州", "木曽"],
}


def get_code(code_name_list: list):
    """Get code.

    Args:
        code_name_list (list[str]): List of Code name. You can choose from the following.
        - PREFECTURES_JP_CODE
        - PREFECTURES_EN_CODE
        - REGION_JP_CODE
        - REGION_JP_CONTENTS
        - NAGANO_SPLIT_10
        - NAGANO_SPLIT_3

    Returns:
        code_list (list[dict]): List of Code dict.
    """
    code_list = []
    for code_name in code_name_list:
        code_list.append(eval(code_name))

    return code_list
