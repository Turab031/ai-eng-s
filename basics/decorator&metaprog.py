# # # decorator is a fun that takes another function and add extra behvaior and return 
# # def my_decorator(func):
# #     def wrapper():
# #         print("before function call")
# #         func()
# #         print("after function call")
# #     return wrapper

# # def say_hello():
# #     print("hello")


# # decorated_fun = my_decorator(say_hello)
# # decorated_fun()


# # # say_hello= my_decorator(say_hello)
# # @my_decorator
# # def say_hello():
# #     print("hello")

# # say_hello()


# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("before function call")
#         result = func(*args,**kwargs)
#         print("after funcion call")
#         return result

#     return wrapper

# @my_decorator
# def add(a,b):
#     return a+b

# print(add(10,20))


import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        