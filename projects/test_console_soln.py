import pytest
from .console_soln import AirBNBCommand

@pytest.fixture
def setUp():
    return AirBNBCommand()

def test_do_emptyline(setUp, capfd):
    setUp.do_emptyline()
    out, err = capfd.readouterr()
    assert out == ''
