'''Dictionary utils testing'''

__author__ = '730611189'

from exercises.ex07.dictionary import invert, favorite_color, count

def test_invert_1() -> None:
    '''Testing if invert outputs {'cat': 'dog'}'''
    test_dict: dict[str, str] = {'dog': 'cat'}
    assert invert(test_dict) == {'cat': 'dog'}

def test_invert_2() -> None:
    '''Testing if invert outputs {'michael': 'jordan', 'larry': 'bird, 'magic': 'johnson'}'''
    test_dict: dict[str, str] = {'jordan': 'michael', 'bird': 'larry', 'johnson': 'magic'}
    assert invert(test_dict) == {'michael': 'jordan', 'larry': 'bird', 'magic': 'johnson'}

def test_invert_3() -> None:
    '''Testing if invert outputs KeyError'''
    test_dict: dict[str, str] = {'dog': 'bird', 'cat': 'fly'}
    assert invert(test_dict) == {'bird': 'dog', 'fly': 'cat'}

def test_favorite_color_1() -> None:
    '''Testing if favorite_color outputs 'blue' '''
    test_dict: dict[str, str] = {'mark': 'blue', 'roy': 'red', 'brent': 'blue'}
    assert favorite_color(test_dict) == 'blue'

def test_favorite_color_2() -> None:
    '''Testing if favorite_color outputs 'red' '''
    test_dict: dict[str, str] = {'mark': 'blue', 'roy': 'red', 'brent': 'red'}
    assert favorite_color(test_dict) == 'red'

def test_favorite_color_3() -> None:
    '''Testing if favorite_color outputs 'yellow' '''
    test_dict: dict[str, str] = {'mark': 'yellow', 'roy': 'yellow', 'brent': 'blue'}
    assert favorite_color(test_dict) == 'yellow'

def test_count_1() -> None:
    '''Testing if favorite_color outputs {'red': 1, 'green': 2, 'blue': 1} '''
    test_list: list[str] = ['red', 'green', 'blue', 'green']
    assert count(test_list) == {'red': 1, 'green': 2, 'blue': 1}

def test_count_2() -> None:
    '''Testing if favorite_color outputs {'red': 3, 'green': 1} '''
    test_list: list[str] = ['red', 'red', 'red', 'green']
    assert count(test_list) == {'red': 3, 'green': 1}

def test_count_3() -> None:
    '''Testing if favorite_color outputs {'yellow': 1, 'green': 2, 'orange': 1} '''
    test_list: list[str] = ['yellow', 'green', 'orange', 'green']
    assert count(test_list) == {'yellow': 1, 'green': 2, 'orange': 1}


