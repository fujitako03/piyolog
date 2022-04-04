import os
import re
from pathlib import Path
from pandas import DataFrame
from typing import List

from .events import (
    Poop,
    Pee,
    BresastMilk,
    Milk,
    Bath,
    BodyTemperature
)

class Piyolog:
    def __init__(
        self,
        data_path
    ):
        self.data_path = Path(data_path)
        self.raw_text = self._read_files(self.data_path)
        self.split_raw_text = self._split_by_date()
        self.baby_name = None
        self.baby_birth = None
        self.events = None

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
    
    def _split_by_date(self):
        split_text = "----------"
        return self.raw_text.split(split_text)

    def _get_name(self) -> str:
        pattern = r'(.+)\([0-9]+歳[0-9]+か月[0-9]+日\)'
        name = re.search(pattern, self.raw_text)
        name.group()
    
if __name__=="__main__":
    piyo = Piyolog(
        data_path ="../../tests/test_data"
    )
    print(piyo._get_name())



