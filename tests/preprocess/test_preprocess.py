import pytest
import datetime

from piyolog import __version__
from piyolog.src.preprocess import PrepRawData

@pytest.mark.parametrize('raw_text, name', [
    ("""【ぴよログ】2022年3月

----------
2022/3/1(火)
ベビー (0歳0か月11日)

00:05 寝る

----------
2022/3/2(水)
ベビー (0歳0か月12日)
"""
, "ベビー"),
    ("""【ぴよログ】2022年3月

----------
2022/3/1(火)
絵文字⏰☻を使った名前 (0歳0か月12日)

00:05 寝る

----------
2022/3/2(水)
絵文字⏰☻を使った名前 (0歳0か月12日)
"""
, "絵文字⏰☻を使った名前"),
])
def test_baby_name(raw_text, name):
    prep = PrepRawData(
        raw_text=raw_text
    )
    prep.preprocess()
    assert prep.baby_name == name


@pytest.mark.parametrize('raw_text, birth', [
    ("""【ぴよログ】2022年3月

----------
2022/3/1(火)
ベビー (0歳0か月11日)

00:05 寝る

----------
2022/3/2(水)
ベビー (0歳0か月12日)
"""
, datetime.date(2022,2,18)),
    ("""【ぴよログ】2022年3月

----------
2022/3/1(火)
絵文字⏰☻を使った名前 (1歳1か月11日)

00:05 寝る

----------
2022/3/2(水)
絵文字⏰☻を使った名前 (1歳1か月12日)
"""
, datetime.date(2021,1,18)),
])
def test_baby_birth(raw_text, birth):
    prep = PrepRawData(
        raw_text=raw_text
    )
    prep.preprocess()
    assert prep.baby_birth == birth

# TODO 1950年よりも前の時のエラーを追加


@pytest.mark.parametrize('raw_text, cleaned_text', [
    ("""【ぴよログ】2022年3月

----------
2022/3/1(火)
ベビー (0歳0か月11日)

00:05 寝る
23:55 うんち

母乳合計　　 左 28分 / 右 29分
ミルク合計　 5回 110ml
搾母乳合計 1回 60ml
睡眠合計　　 13時間55分
おしっこ合計 13回
うんち合計　 8回

----------
2022/3/2(水)
ベビー (0歳0か月12日)

01:40 寝る
23:10 おしっこ

母乳合計　　 左 33分 / 右 26分
ミルク合計　 4回 120ml
睡眠合計　　 15時間10分
おしっこ合計 11回
うんち合計　 6回

----------
"""
, 
"""----------
2022/3/1(火)
00:05 寝る
23:55 うんち
----------
2022/3/2(水)
01:40 寝る
23:10 おしっこ
----------
""")
])
def test_remove_without_logs(raw_text, cleaned_text):
    prep = PrepRawData(
        raw_text=raw_text
    )
    prep.preprocess()
    assert prep._raw_text_cleaned == cleaned_text


@pytest.mark.parametrize('raw_text, day_texts', [
    ("""【ぴよログ】2022年3月

----------
2022/3/1(火)
ベビー (0歳0か月11日)

00:05 寝る
23:55 うんち

母乳合計　　 左 28分 / 右 29分
ミルク合計　 5回 110ml
搾母乳合計 1回 60ml
睡眠合計　　 13時間55分
おしっこ合計 13回
うんち合計　 8回

----------
2022/3/2(水)
ベビー (0歳0か月12日)

01:40 寝る
23:10 おしっこ

母乳合計　　 左 33分 / 右 26分
ミルク合計　 4回 120ml
睡眠合計　　 15時間10分
おしっこ合計 11回
うんち合計　 6回

----------
""",
  [
"""2022/3/1(火)
00:05 寝る
23:55 うんち
"""
,
"""2022/3/2(水)
01:40 寝る
23:10 おしっこ
"""
    ])
])
def test_split_all_into_day(raw_text, day_texts):
    prep = PrepRawData(
        raw_text=raw_text
    )
    prep.preprocess()
    assert prep.day_texts == day_texts

    # [
    #     {
    #         "date":datetime.date(2022,3,1),
    #         "logs":["00:05 寝る", "23:55 うんち"],
    #     },
    #     {
    #         "date":datetime.date(2022,3,2),
    #         "logs":["01:40 寝る", "23:10 おしっこ"],
    #     },
    # ])
