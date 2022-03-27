
import os
from pathlib import Path
from typing import List

class Piyolog:
    def __init__(
        self,
        data_path
    ):
        self.data_path = Path(data_path)

    @staticmethod
    def _read_files(
        data_path: Path
    ) -> List[str]:
        return [d.read_text() for d in data_path.iterdir()] 

