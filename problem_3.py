m=int(input("Enter number of order:"))
order = []
i=1
while i <= m:
    l=input("order:")
    order.append(l)
    i=i+1
order.reverse()
def get_order(order):
    while len(order)>0:
        popped = order.pop()  
        print("Preparing your order:", popped)

print("The following orders have been dispatched:")
while len(order)>0:
        popped = order.pop()  
        print(popped)

get_order(order)
