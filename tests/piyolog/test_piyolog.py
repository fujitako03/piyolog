from piyolog import __version__

from pathlib import Path

from piyolog import read_log
from piyolog.src.piyolog import Piyolog


def test_version():
    assert __version__ == '0.1.0'


def test_read_log():
    """ピヨログデータを読み込む正常テスト
    """
    data = "./tests/test_data"
    piyo = read_log(data=data)
    assert type(piyo) is Piyolog


def test__read_files():
    """ピヨログデータを読み込む正常テスト
    """
    data = "./tests/test_data"
    piyo = Piyolog(data_path=data)
    
    assert piyo.text[:13] == "【ぴよログ】2022年3月"
