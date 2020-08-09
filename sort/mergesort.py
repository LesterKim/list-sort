from sort.utilities.numbers import Numbers
from sort.sort import sort


def mergesort(numbers: Numbers) -> Numbers:
  return sort(numbers, 'mergesort')


def merge(left: Numbers, right: Numbers) -> Numbers:
  merged_numbers = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged_numbers.append(left[i])
      i += 1
    else:
      merged_numbers.append(right[j])
      j += 1

  for index, numbers in ((i, left), (j, right)):
    while index < len(numbers):
      merged_numbers.append(numbers[index])
      index += 1

  return merged_numbers