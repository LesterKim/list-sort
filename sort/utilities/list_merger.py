from sort.numbers import Number, Numbers


class ListMerger:
  def __init__(self, left: Numbers, right: Numbers) -> None:
    self._i = self._j = 0
    self._left = left
    self._right = right
    self._merged_numbers = []

  def merge(self) -> Numbers:
    while self._i < len(self._left) and self._j < len(self._right):
      self._append_smallest_remaining_number()

    return self._append_remaining_numbers()

  @property
  def _left_number(self) -> Number:
    return self._left[self._i]

  @property
  def _right_number(self) -> Number:
    return self._right[self._j]

  def _append_remaining_numbers(self) -> Numbers:
    for index, numbers in ((self._i, self._left), (self._j, self._right)):
      self._merged_numbers.extend(numbers[index:])

    return self._merged_numbers

  def _append_smallest_remaining_number(self) -> None:
    if self._left_number < self._right_number:
      self._merged_numbers.append(self._left_number)
      self._i += 1
    else:
      self._merged_numbers.append(self._right_number)
      self._j += 1