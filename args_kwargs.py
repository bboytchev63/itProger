# This does not scale well 
# def tea_order(customer_name, tea_type, milk=None, sweetener=None ):
#     print(customer_name, "ordered a", tea_type, "tea")
#     if milk != None:
#         print(" - Add:", milk)
#     if sweetener != None:
#         print(" - Add Sweetener")

# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", "oat")
# tea_order("Marla", "green", "oat", "honey")
# This does not scale well 
# Need to be more flexible with number of arguments
# USING *ARGUMENTS AS TUPLE
# def tea_order(customer_name, tea_type, *args):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for arg in args:
#         print(" --- add : ",arg)

# # You can use *args, *arguments, *Anything
# # this is a tuple
# #   
# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", "oat")
# tea_order("Marla", "green", "oat", "honey")


# # USING **ARGUMENTS AS DICTIONARY
# def tea_order(customer_name, tea_type, **kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key , value in kwargs.items():
#         print("a add ", key, value)

# # You can use **kwargs, **arguments, **Anything
# # this is variable a dictionary
# #   
# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", milk = "oat")
# tea_order("Marla", "green", milk = "oat", sweetener = "honey")

# Can use *args and **kwargs together
# def tea_order(customer_name, tea_type, *args, ** kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for arg in args:
#         print(" - Add", arg)
#     for key, value in kwargs.items():
#         print(" - Add", key, ":", value)

# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", milk="oat")
# tea_order("Tony", "black", "oat", sweetener="honey")
# !!! positional *args place before  ** kwargs

# Also we can use * and ** as func param
def tea_order(customer_name, tea_type, *args, ** kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print(" - Add", arg)
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)

eves_extras = ("almond", "shugar", "lemon")
tea_order("Gogo","black",*eves_extras)

eves_extras = {"milk": "almond", "sweetener": "sugar", "flavor": "lemon"}
tea_order("Eve", "green", milk="almond", sweetener="sugar", flavor="lemon")
tea_order("Eve", "green", ** eves_extras)