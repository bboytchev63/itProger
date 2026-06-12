def tea_order(customer_name, tea_type, milk=None):

print(customer_name, "ordered a", tea_type, "tea")
if milk != None:
print(" - Add:", milk)|

tea_order("Alice", "chamomile")
tea_order("Bob", "black", "oat")

