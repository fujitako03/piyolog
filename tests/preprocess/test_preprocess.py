import pytest

from piyolog import __version__
from piyolog.src.preprocess import PrepRawData

def test_baby_name():
    raw_text ="""【ぴよログ】2022年3月

----------
2022/3/1(火)
ベビー (0歳0か月11日)

00:05 寝る
02:45 おしっこ
02:50 起きる (2時間45分)
02:55 母乳 左 2分 → 右 4分
03:00 ミルク 30ml
03:10 寝る
03:15 うんち
"""
    prep = PrepRawData(
        raw_text=raw_text
    )
    prep.preprocess()
    assert prep.baby_name == "ベビー"