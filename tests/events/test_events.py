import datetime
import pytest

from piyolog import __version__
from piyolog.src.events import (
    Event,
    Poop,
    BresastFooding,
    Milk,    
    BodyTemperature,
    Height,
    Weight,
    Chest,
    BreastMilk,
    Drink,
    Vaccination,
    Milking,
    Walking,
)


@pytest.mark.parametrize('memo', [
    (None),
    ("サンプルのメモです"),
])
def test_event(memo):
    name_ja = 'お風呂'
    event_datetime = datetime.datetime.now()
    event = Event(
        name_ja=name_ja,
        event_datetime=event_datetime,
        memo=memo
        )
    assert type(event) is Event


@pytest.mark.parametrize('memo', [
    (None),
    ("サンプルのメモです"),
])
def test_poop(memo):
    name_ja = 'うんち'
    event_datetime = datetime.datetime.now()
    amount = "ふつう"
    hardness = "ふつう"
    ins = Poop(
        name_ja=name_ja,
        event_datetime=event_datetime,
        amount=amount,
        hardness=hardness,
        memo=memo
        )
    assert type(ins) is Poop


@pytest.mark.parametrize('memo', [
    (None),
    ("サンプルのメモです"),
])
def test_bresastfooding(memo):
    name_ja = '母乳'
    event_datetime = datetime.datetime.now()
    amount = 10
    left_minutes = 5
    right_minutes = 5
    order = 'R_L'
    ins = BresastFooding(
        name_ja=name_ja,
        event_datetime=event_datetime,
        amount=amount,
        left_minutes=left_minutes,
        right_minutes=right_minutes,
        order=order,
        memo=memo
        )
    assert type(ins) is BresastFooding