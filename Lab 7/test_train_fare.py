from hypothesis import given, strategies as st
from train_fare import parse_pnr, journey_distance, berth_type
import pytest
@given(st.text() | st.none())
def test_parse_pnr_no_crash(s):
    try:
        parse_pnr(s)
    except Exception as e:
        pytest.fail(f"parse_pnr crashed with input {s!r}: {e}")  
@given(st.text() | st.none())
def test_journey_distance_no_crash(s):
    try:
        journey_distance(s)
    except Exception as e:
        pytest.fail(f"journey_distance crashed with input {s!r}: {e}")
@given(st.text() | st.none())
def test_berth_type_no_crash(s):
    try:
        berth_type(s)
    except Exception as e:
        pytest.fail(f"berth_type crashed with input {s!r}: {e}")