import pytest

from employee import Employee

@pytest.fixture
def employee():
    """create an employee for use in tests"""
    return Employee('John', 'Doe', 50000)
def test_give_default_raise(employee):
    """test that the default raise is added to the salary"""
    employee.give_raise()
    assert employee.salary == 55000
def test_give_custom_raise(employee):
    """test that a custom raise is added to the salary"""
    employee.give_raise(10000)
    assert employee.salary == 60000