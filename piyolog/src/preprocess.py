from __future__ import annotations

import re
import datetime
from dateutil.relativedelta import relativedelta

class PrepRawData:
    def __init__(
        self,
        raw_text
    ) -> None:
        self.raw_text = raw_text
    
    def preprocess(self):
        # 全体の属性取得
        self._baby_name = self._get_baby_name()
        self._baby_birth = self._get_birth()
        
        # 不要な箇所を除去
        self._raw_text_cleaned =  self._remove_without_logs()

        # 日別に分割する
        self._day_texts = self._split_all_into_day()
        
        # 日別の属性を取得
        self._day_attributes = self._get_day_attributes()
        
        # イベント別に分割し、イベント別の属性を取得
        self._events_prepared = self._split_day_into_event()
        
        # イベント種類ごとに前処理を実施
        self._events = self._preprocess_by_event()

    @property 
    def events(self):
        return self._events
    
    @property
    def baby_name(self):
        return self._baby_name
    
    @property
    def baby_birth(self):
        return self._baby_birth
    
    def _get_baby_name(self) -> str:
        """生データから子供の名前を取得する

        Returns:
            str: 子供の名前
        """
        pattern = r'(\S+)\s+\([0-9]+歳[0-9]+か月[0-9]+日\)'
        match = re.search(pattern, self.raw_text)
        try:
            name = match.group(1)
            return name
        except:
            return ""
        

    def _get_birth(self) -> datetime.date:
        """生データから誕生日を取得する

        Returns:
            date: 誕生日
        
        Rases:
            誕生日が1950年以前
        """
        # 記録日の情報をパース
        pattern_today = r'(\d{4}\/\d+\/\d+)'
        match_today = re.search(pattern_today, self.raw_text)
        str_today = match_today.group(1)
        date_today = datetime.datetime.strptime(str_today, "%Y/%m/%d").date()

        # 生後日数の情報をパース
        pattern_age = r'\((\d+)歳(\d+)か月(\d+)日\)'
        match_age = re.search(pattern_age, self.raw_text)
        age_year  = int(match_age.group(1))
        age_month  = int(match_age.group(2))
        age_days  = int(match_age.group(3))
        
        # 演算して誕生日を求める（注:日付から計算しないと結果が変わる）
        birth_day = date_today - \
            relativedelta(days=age_days) - \
            relativedelta(months=age_month) - \
            relativedelta(years=age_year)

        if birth_day < datetime.date(1950, 1, 1):
            raise ValueError("誕生日が1950年よりも前です。値を確認してください")
        
        return date_today - relativedelta(days=age_days) - relativedelta(months=age_month) - relativedelta(years=age_year)
    
    def _remove_without_logs(self) -> str:
        """生データからログ以外の不要な箇所を除去する

        Returns:
            str: 不要な箇所を除去したテキスト
        """
        # 正規表現パターンの定義
        pattern_line = r"\-+" # 区切り線
        pattern_date = r"\d{4}/\d+/\d+\(\S\)" # 日付
        pattern_log = r"\d{2}:\d{2}.+" # ログ
        pattern_concat = "|".join([
            pattern_line,
            pattern_date,
            pattern_log,
        ])

        # 1.行ごとに分割
        split_rows = self.raw_text.split('\n')

        # 2.条件に当てはまらないものは除く
        use_rows = [
            row
            for row
            in split_rows
            if re.match(pattern_concat, row)
        ]

        # 結合して返す
        return "\n".join(use_rows) + "\n"

    def _split_all_into_day(self) -> list[str]:
        """全体を日別に分割し、日別のテキストを返す

        Return:
        list[str]: 日別の属性リスト
    """
        split_text = "----------\n"
        cleaned_text = [
            text 
            for text 
            in self._raw_text_cleaned.split(split_text) 
            if not text in ("", "\n")]
        
        return cleaned_text
    
    def _get_day_attributes(self) -> list[dict]:
        """日別のテキストから、日別の属性を返す

        Returns:
            list[dict]: _description_
        """
        list_attributes = []
        for day_text in self._day_texts:
            # 日付を抽出
            pattern_date = r"\d{4}/\d+/\d+"
            m = re.match(pattern_date, day_text)
            log_date = datetime.datetime.strptime(m.group(), "%Y/%m/%d").date()
            
            # logを抽出
            pattern_log_text = r"\d{4}/\d+/\d+\(\S\)\n"
            log_text = re.sub(pattern_log_text, "", day_text) # 日付部分を削除

            list_attributes.append({
                "date": log_date,
                "age_days": (log_date - self.baby_birth).days,
                "log_text": log_text,
            })
        return list_attributes

    def _split_day_into_event(
        self
    ) -> list[tuple]:
        """日付ごとのテキストをイベント単位に分割する

        Returns:
            list[dict]: イベント単位のリスト
        """
        # 日付ごとのテキストをイベント単位の行ごとに分割
        event_lines = []
        for day in self._day_attributes:
            events_info = [
                {"date": day.get("date"),
                "age_days": day.get("age_days"),
                "event_all_text": text
                } 
            for text
            in day.get("log_text").split("\n")
            if text != ""] # 最後の改行以降は除く
            event_lines.extend(events_info)

        # 行ごとにループを回し、前処理する
        event_attributes_list = []
        for line in event_lines:
            event_datetime = self._get_event_datetime(date=line.get("date"), text=line.get("event_all_text"))
            event_name, event_text = self._split_event_name_text(text=line.get("event_all_text"))
            
            event_attributes_list.append(
                {"datetime": event_datetime,
                "age_days":line.get("age_days"),
                "event_name": event_name,
                "event_text": event_text})
        
        return event_attributes_list
   
    @staticmethod
    def _get_event_datetime(
        date: datetime.date,
        text: str,
    ) -> datetime:
        """行ごとに分割したテキストと日付から、イベント情報を抽出したタプルを作成する

        Args:
            date (datetime.date): 行に対応する日付
            text (str): 行ごとに分割したテキスト

        Returns:
            event_datetime: イベント日時
        """
        time_str = text.split(" ")[0]
        print(time_str)
        time_datetime = datetime.datetime.strptime(time_str, "%H:%M")
        return datetime.datetime(date.year, date.month, date.day, time_datetime.hour, time_datetime.minute)

    @staticmethod
    def _split_event_name_text(
        text: str,
    ) -> str:
        """行ごとに分割したテキストを、イベント名と説明テキストに分割する

        Args:
            text (str): 行ごとに分割したテキスト

        Returns:
            str, str: イベント名、イベントテキスト
        """
        split_text = text.split(" ")
        return split_text[1], " ".join(split_text[2:])

    def _preprocess_by_event(
        self
    ) -> list[Event]:
        pass