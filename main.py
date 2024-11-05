def sort_even_odd(numbers):
  """Sorts a list of numbers into even and odd sub-lists.

  Args:
    numbers: A list of integers.

  Returns:
    A tuple containing two lists: even_numbers and odd_numbers.
  """

  even_numbers = []
  odd_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      odd_numbers.append(number)

  # Sort the even and odd lists
  even_numbers.sort()
  odd_numbers.sort()

  return even_numbers, odd_numbers

# Example usage
numbers = [1, 4, 7, 2, 9, 5, 8, 3, 6]

even_numbers, odd_numbers = sort_even_odd(numbers)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)