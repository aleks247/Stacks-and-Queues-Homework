pallet = list(map(int, input().split()))
shelf_capacity = int(input())

stack = []

used_shelves = 0
current_shelf_capacity = 0

for item in pallet:
    if current_shelf_capacity + item <= shelf_capacity:
        current_shelf_capacity += item
        stack.append(item)
    else:
        used_shelves += 1
        while stack:
            current_shelf_capacity -= stack.pop()
        current_shelf_capacity += item
        stack.append(item)

if current_shelf_capacity > 0:
    used_shelves += 1

print(used_shelves)
