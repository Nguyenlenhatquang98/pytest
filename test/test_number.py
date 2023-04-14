import pytest
from pytest_bdd import given,then,when,parsers

# scenarios('check_number.feature')

# @scenario('check_number.feature', "I'm learning coding")
# def test_number():
#     pass

@given(parsers.parse('I have a number {num1}'),target_fixture='num')
def number(num1):
    return int(num1)

@when(parsers.parse('I multiple that with number {num2}'),target_fixture='mul_num')
def mul_number(num,num2):
    return num * int(num2)

@then(parsers.parse('I verify that with number {num3}'))
def verify_equal(mul_num,num3):
    assert mul_num == int(num3)

