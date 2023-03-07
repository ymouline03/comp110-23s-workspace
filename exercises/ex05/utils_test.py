'''Utils testing'''
__author__ = '730611189'

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens() -> None:
    '''Testing if only_evens outputs [2, 4, 6]'''
    test_list: list[int] = [2, 3, 4, 5, 6, 7]
    assert only_evens(test_list) == [2, 4, 6]

def test_concat() -> None:
    '''Testing if concat outputs [3, 7, 5, 7, 4, 5]'''
    test_list_1: list[int] = [3, 7, 5]
    test_list_2: list[int] = [7, 4, 5]
    assert concat(test_list_1, test_list_2) == [3, 7, 5, 7, 4, 5]

def test_sub() -> None:
    '''Testing if sub outputs [0, 6]'''
    test_list: list[int] = [9, 2, 0, 6, 3]
    test_start_idx = 2
    test_end_idx = 4
    assert sub(test_list, test_start_idx, test_end_idx) == [0, 6]