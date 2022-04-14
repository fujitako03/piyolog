import re

class PrepRawData:
    def __init__(
        self,
        raw_text
    ) -> None:
        self.raw_text = raw_text
        self.baby_name = None
        self.baby_birth = None
        self.events = None
    
    def preprocess(self):
        # TODO 一連の前処理を実行
        self.baby_name = None
        self.baby_birth = None
        self.events = None
    
    def _split_by_date(self):
        split_text = "----------"
        return self.raw_text.split(split_text)

    def _get_name(self) -> str:
        pattern = r'(.+)\([0-9]+歳[0-9]+か月[0-9]+日\)'
        name = re.search(pattern, self.raw_text)
        name.group()
    
    
