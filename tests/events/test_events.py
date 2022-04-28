import datetime
import pytest

from piyolog import __version__
from piyolog.src.events import (
    Event,
)


# @pytest.mark.parametrize('description, amount_ml, memo', [
#     ("60ml", 60, ""),
#     ("460ml   吐き戻し多め", 460, "吐き戻し多め"),
# ])
# def test_event_milk(description, amount_ml, memo):
#     name = 'ミルク'
#     event_datetime = datetime.datetime.now()
    
#     event = Event(
#         name=name,
#         event_datetime=event_datetime,
#         description=description
#        )

#     assert event.amount_ml == amount_ml
#     assert event.memo == memo

