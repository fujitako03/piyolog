from piyolog import __version__

from pathlib import Path
from pandas import DataFrame

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

def test_get_events_default():
    """ぴよログの各イベントをDF形式で取得する
    """
    data = "./tests/test_data"
    piyo = read_log(data=data)
    df_event = piyo.get_events()
    assert type(df_event) is DataFrame

def test_get_events_specific():
    """ぴよログの各イベントをDF形式で取得する
    """
    data = "./tests/test_data"
    piyo = read_log(data=data)
    df_event = piyo.get_events(event="うんち")
    assert type(df_event) is DataFrame



def test__read_files():
    """ピヨログデータを読み込む正常テスト
    """
    data = "./tests/test_data"
    piyo = Piyolog(data_path=data)
    
    assert piyo._raw_text.count("\n") == 3325
