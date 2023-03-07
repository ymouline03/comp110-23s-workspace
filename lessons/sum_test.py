from lessons.sum import sum

def test_sum() -> None:
    test_list: list[float] = [1.0, 2.3, 5.7, 3.0]
    assert sum(test_list) == 12.0