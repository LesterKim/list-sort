from sort.numbers import Numbers
from sort.runtime_printer import runtime_printer
from sort.utilities.sort import sort


class ListSorter:
  def __init__(self, numbers: Numbers) -> None:
    self._numbers = numbers

  @runtime_printer
  def sort(self) -> Numbers:
    return sort(self._numbers, 'mergesort')

sorted = runtime_printer(sorted)

numbers = [8, -9, 0, 222, 81, 53, 45, 99, -88, 344, 146, -958, 222, 353, 0, -2, 222, 0, 0, 8, -9, 0, 222, 81, 53, 45, 99, -88, 344, 146, -958, 222, 353, 0, -2, 222, 0, 0, -958, 222, 353, 0, -2, 222, 0, 0, 8, -9, 0, 222, 81, 53, 45, 99, -88]
assert ListSorter(numbers).sort() == sorted(numbers)

# n = 2 ** 19
# numbers = list(range(n - 1, 0, -1))
# assert ListSorter(numbers).sort() == list(range(1, n))