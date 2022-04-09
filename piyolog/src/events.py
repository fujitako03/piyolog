import datetime
from typing import str, int

class Event:
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        memo:str=None 
    ):
        self.name_ja = name_ja
        self.evet_datetime = event_datetime
        self.memo = memo

    def check_name_ja(self, except_name_ja) -> None:
        """イベント名が正しいかチェックし、間違っていた場合にエラー

        Args:
            except_name_ja (str): 正しいイベント名
        """
        if self.name_ja != except_name_ja:
            ValueError(f'The class excepted {except_name_ja} but got {self.name_ja}')


class Poop(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        amount: str,
        hardness: str,
        memo:str=None,
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.amount = amount
        self.hardness = hardness

        # check values
        self.check_name_ja('うんち')

class BresastFooding(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        left_minutes : int,
        right_minutes: int,
        order: str,
        amount : int,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.left_minutes = left_minutes
        self.right_minutes = right_minutes
        self.order = order
        self.amount = amount

        # check values
        self.check_name_ja('母乳')

class Milk(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        amount : int,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.amount = amount

        # check values
        self.check_name_ja('ミルク')

class BodyTemperature(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        temperature : float,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.temperature = temperature

        # check values
        self.check_name_ja('体温')

class Height(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        height : float,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.height = height

        # check values
        self.check_name_ja('身長')

class Weight(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        weight : float,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.weight = weight

        # check values
        self.check_name_ja('体重')

class Chest(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        measurement : float,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.measurement = measurement

        # check values
        self.check_name_ja('胸囲')

class BreastMilk(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        amount :int,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.amount = amount

        # check values
        self.check_name_ja('搾母乳')

class Drink(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        amount :int,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.amount = amount

        # check values
        self.check_name_ja('のみもの')

class Vaccination(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        vaccine :str,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.vaccine = vaccine

        # check values
        self.check_name_ja('予防接種')

class Milking(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        amount :int,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.amount = amount

        # check values
        self.check_name_ja('搾乳')

class Walking(Event):
    def __init__(
        self,
        name_ja :str,
        event_datetime :datetime.datetime,
        amount :int,
        memo:str=None 
    ):
        super().__init__(
            name_ja,
            event_datetime,
            memo)
        self.amount = amount

        # check values
        self.check_name_ja('さんぽ')

