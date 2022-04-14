import os
from pathlib import Path
from pandas import DataFrame
from typing import List

from .preprocess import PrepRawData

from .events import (
    Poop,
    BresastFooding,
    Milk,
    BodyTemperature,
    Height,
)

class Piyolog:
    def __init__(
        self,
        data_path
    ):
        self.data_path = Path(data_path)
        self._raw_text = self._read_files(self.data_path)
        
        # 前処理
        prep = PrepRawData(raw_text = self._raw_text)
        prep.preprocess()
        self.events = prep.events
        self.baby_name = prep.baby_name
        self.baby_birth = prep.baby_birth

    def get_events(
        self,
        event:str =None
    ) -> DataFrame:
        """指定したイベントのログをデータフレーム形式で出力する

        Args:
           event (str, optional): イベント名. Defaults to None.

        Returns:
            DataFrame: 指定したイベントのログをまとめたデータフレーム
        """
        if event is None:
            # Return all events
            df = DataFrame()
            return df
        else:
            # Return specified events
            df = DataFrame()
            return df

    @staticmethod
    def _read_files(
        data_path: Path
    ) -> str:
        return "\n".join([d.read_text() for d in data_path.iterdir()])


if __name__=="__main__":
    piyo = Piyolog(
        data_path ="../../tests/test_data"
    )
    print(piyo._get_name())



