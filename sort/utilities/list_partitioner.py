from random import shuffle

from sort.numbers import Numbers


class ListPartitioner:
  def __init__(self, numbers: Numbers) -> None:
    shuffle(numbers)
    self._numbers = numbers
    self._numbers_length = len(numbers)
    self._pivot = numbers[-1]
    self._pivot_index = 0

  def partition(self) -> int:
    self._put_numbers_smaller_than_or_equal_to_pivot_to_the_left()
    self._swap_numbers(self._last_index, self._pivot_index)

    return self._pivot_index

  @property
  def _last_index(self):
    return self._numbers_length - 1

  def _put_numbers_smaller_than_or_equal_to_pivot_to_the_left(self):
    for i in range(self._last_index):
      if self._numbers[i] <= self._pivot:
        self._swap_numbers(i, self._pivot_index)
        self._pivot_index += 1

  def _swap_numbers(self, i: int, j: int) -> None:
    self._numbers[i], self._numbers[j] = self._numbers[j], self._numbers[i]