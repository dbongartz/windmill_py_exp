import pytest
from windmill import Windmill


def test_windmill_init():
    dut = Windmill()
    assert 0 == dut.rotations


def test_windmill_rotation():
    dut = Windmill()
    windspeed_ms = 7
    duration_s = 500
    expected = 7*500

    dut.receive_wind(windspeed_ms, duration_s)
    assert expected == dut.rotations

    # Missing: change windspeed once and change duration once


# pytest.main()
