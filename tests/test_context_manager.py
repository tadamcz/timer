import time
import pytest
from timer.timer import Timer

def test_timer_context_manager():
    with Timer(name="test") as t:
        time.sleep(1)
    assert t is not None
    assert t.last > 0
    assert "'test' elapsed time:" in t.text