from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

biggest_order = max(orders)

while orders:
    current_order = orders.popleft()
    
    if current_order <= food_quantity:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        break

if not orders:
    print(biggest_order)
    print("Orders complete")
else:
    remaining_orders = ', '.join(map(str, orders))
    
    print(biggest_order)
    print(f"Orders left: {remaining_orders}")
