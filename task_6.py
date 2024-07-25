# Creating a list of numbers
numbers = [5, 2, 9, 1, 5, 6]
# Printing the list
print("List of numbers:", numbers)
# Access list elements using indexing
first_element = numbers[0]
last_element = numbers[-1]
print("First element:", first_element)
print("Last element:", last_element)
#list methods like append(), remove(), and sort()
numbers.append(10)
print("After appending 10:", numbers)
numbers.remove(1)
print("After removing 1:", numbers)
numbers.sort()
print("Sorted list:", numbers)


#Program to find second largest element in an array
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]
numbers = [5, 2, 9, 1, 5, 6]
second_largest_number = second_largest(numbers)
print("Second largest number:", second_largest_number)


# Program to sort even and odd elements of array separately.
def sort_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers.sort()
    odd_numbers.sort()
    return even_numbers, odd_numbers
numbers = [5, 2, 9, 1, 5, 6]
sorted_evens, sorted_odds = sort_even_odd(numbers)
print("Sorted even numbers:", sorted_evens)
print("Sorted odd numbers:", sorted_odds)

