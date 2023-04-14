from pytest_bdd import scenario
from test_number import *

@scenario('check_number.feature', "I'm learning coding")
def test_number_successfully():
    pass

@scenario('check_number.feature', "I'm learning coding failed")
def test_number_failed():
    pass

# scenarios('check_number.feature')