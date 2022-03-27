from piyolog import __version__

from piyolog import read_log
from piyolog.src.piyolog import Piyolog


def test_version():
    assert __version__ == '0.1.0'


def test_read_log():
    """ピヨログデータを読み込む正常テスト
    """
    data = "./test_data"
    piyo = read_log(data=data)
    assert type(piyo) is Piyolog
