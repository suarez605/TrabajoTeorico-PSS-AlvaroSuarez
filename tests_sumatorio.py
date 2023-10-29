import pytest
from app import sum

def test_sum_1():
  assert sum(1, 2) == 3

def test_sum_2():
  assert sum(1, -2) == -1