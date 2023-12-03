from kaitenzushi.solve import get_maximum_eaten_dish_count

def test_get_maximum_eaten_dish_count() -> None:
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 1
    res = get_maximum_eaten_dish_count(N, D, K)
    assert res == 5, res

    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 2
    res = get_maximum_eaten_dish_count(N, D, K)
    assert res == 4, res

    N = 7
    D = [1, 2, 1, 2, 1, 2, 1]
    K = 2
    res = get_maximum_eaten_dish_count(N, D, K)
    assert res == 2, res
