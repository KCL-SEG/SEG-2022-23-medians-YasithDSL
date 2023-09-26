"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
if len(numbers) % 2 == 0:
    l = len(numbers)
    left = numbers[int((l / 2) - 1)]
    right = numbers[int((l / 2))]
    print((left + right) / 2)
else:
    print(numbers[(len(numbers) / 2).__floor__()])