from sort.utilities.list_merger import ListMerger
from sort.utilities.list_partitioner import ListPartitioner
from sort.numbers import Numbers


_sorted_list_combiners = {
  'mergesort': lambda left, right: ListMerger(left, right).merge(),
  'quicksort': lambda left, right: left + right,
}

_middle_index_calculators = {
  'mergesort': lambda numbers: len(numbers) // 2,
  'quicksort': lambda numbers: ListPartitioner(numbers).partition(),
}


def sort(numbers: Numbers, sort_type: str = 'quicksort') -> Numbers:
  if len(numbers) < 2:
    return numbers

  middle_index = _middle_index_calculators[sort_type](numbers)
  left = sort(numbers[:middle_index], sort_type)
  right = sort(numbers[middle_index:], sort_type)

  return _sorted_list_combiners[sort_type](left, right)