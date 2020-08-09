from sort.numbers import Numbers
from sort.utilities.runtime_printer import runtime_printer
from sort.utilities.sort import sort


class ListSorter:
  def __init__(self, numbers: Numbers) -> None:
    self._numbers = numbers

  @runtime_printer
  def sort(self) -> Numbers:
    return sort(self._numbers, 'mergesort')
