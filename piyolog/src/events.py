from abc import ABCMeta, abstractmethod
# TODO 各eventクラスは重複するため、抽象クラスを作る

class Event(metaclass=ABCMeta):
    pass
    

class Poop(Event):
    def __init__(
        self
    ):
        self.name_ja = 'うんち'
        self.evet_datetime = None
        self.amount = None
        self.hardness = None
        self.memo = None

class Pee(Event):
    def __init__(
        self
    ):
        self.name_ja = 'おしっこ'
        self.evet_datetime = None
        self.memo = None

class BresastMilk(Event):
    def __init__(
        self
    ):
        self.name_ja = '母乳'
        self.evet_datetime = None
        self.left_time = None
        self.right_time = None
        self.order = None
        self.amount = None
        self.memo = None

class Milk(Event):
    def __init__(
        self
    ):
        self.name_ja = 'ミルク'
        self.evet_datetime = None
        self.amount = None
        self.memo = None

class Bath(Event):
    def __init__(
        self
    ):
        self.name_ja = 'お風呂'
        self.evet_datetime = None
        self.memo = None

class BodyTemperature(Event):
    def __init__(
        self
    ):
        self.name_ja = '体温'
        self.evet_datetime = None
        self.temperature = None
        self.memo = None


