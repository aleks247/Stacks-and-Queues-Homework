pallet = list(map(int, input().split()))
shelf_capacity = int(input())

shelves_used = 0
current_shelf_capacity = 0
stack = []

for item in pallet:
    if current_shelf_capacity + item <= shelf_capacity:
        current_shelf_capacity += item
        stack.append(item)
    else:
        shelves_used += 1
        while stack:
            current_shelf_capacity -= stack.pop()
        current_shelf_capacity += item
        stack.append(item)

if current_shelf_capacity > 0:
    shelves_used += 1

print(shelves_used)
