import datetime

class Event:
    def __init__(
        self,
        name :str,
        event_datetime :datetime.datetime,
        description :str
    ):
        self.name = name
        self.event_datetime = event_datetime
        self.description = description

        # 前処理
        self._preprocess()
    
    def _preprocess(self):
        if self.name == "うんち":
            self._preprocess_poo()
        elif self.name == "おしっこ":
            self._preprocess_pee()
        elif self.name == "ミルク":
            self._preprocess_milk()
        elif self.name == "母乳":
            self._preprocess_breast_fooding()
        elif self.name == "搾母乳":
            self._preprocess_breast_milk()
        elif self.name == "起きる":
            self._preprocess_sleep()
        elif self.name == "身長":
            self._preprocess_height()
        elif self.name == "体重":
            self._preprocess_weight()
        else:
            pass
    
    def _preprocess_poo(self):
        self.amount = ""
        self.hardness = ""
        self.memo = ""
        
    def _preprocess_pee(self):
        self.amount = ""
        self.memo = ""

    def _preprocess_milk(self):
        self.amount_ml = 0
        self.memo = ""

    def _preprocess_breast_fooding(self):
        self.amount_ml = 0
        self.left_minutes = 0
        self.right_minutes = 0
        self.sum_minutes = 0
        self.side_order = []
        self.memo = ""
    
    def _preprocess_breast_milk(self):
        self.amount_ml = 0
        self.memo = ""

    def _preprocess_sleep(self):
        self.sleeping_minuites = 0
        self.fall_asleep_datetime = datetime.datetime.now()
        self.wakeup_datetime = datetime.datetime.now()
        self.memo = ""

    def _preprocess_height(self):
        self.height_cm = 0
        self.memo = ""
        
    def _preprocess_weight(self):
        self.weight_cm = 0
        self.memo = ""
