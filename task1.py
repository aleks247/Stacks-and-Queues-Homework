numbers_list = input("Enter numbers(1, 2, 3...): ")
numbers = numbers_list.split(', ')
reversed_list = ', '.join(numbers[::-1])

print("Reversed list: " + reversed_list)
