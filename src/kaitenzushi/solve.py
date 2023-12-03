def get_maximum_eaten_dish_count(N: int, D: list[int], K: int) -> int:
    """iykyk
    
    Given
    
      N = 6
      D = [1, 2, 3, 3, 2, 1]
      K = 1

    Find the number of D_i such that D_i - K is excluded.
    """
    eaten = {}
    dish_count = 0
    for dish in D:
      if dish not in eaten:
          dish_count += 1
          eaten[dish] = dish_count
      else:
          if eaten[dish] > dish_count - K:
              continue
          else:
              dish_count += 1
              eaten[dish] = dish_count

    return dish_count