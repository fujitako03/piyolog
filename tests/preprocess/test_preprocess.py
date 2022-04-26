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