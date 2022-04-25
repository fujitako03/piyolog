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

