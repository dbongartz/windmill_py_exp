import pytest


import nested

testdata = [(True, True), (False, False)]


@pytest.mark.parametrize("val", testdata)
def test_wrapper(val, mocker):
    mock_add = mocker.patch("nested.do_something_simpler")
    mock_add.return_value = val[0]

    dut = nested.Stuff(1, 2, 3, [42, 43])

    assert nested.do_smothing_wrapper(dut) is val[1]
