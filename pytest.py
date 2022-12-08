import pytest
from main import *


def test_costs():
    assert costs_list() == [150, 1200, 300, 500, 829, 2750]

def test_total():
    assert total(costs_list()) == 6361.0

def test_main():
    assert main() is None