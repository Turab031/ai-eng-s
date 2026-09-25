def greet():
    print("hello")


greet()

def intoduce(name,age):
    print(f"{name} is {age} years old")



intoduce("turab",23)

# keyword args->ise order matter nhi krta
intoduce(age=23,name="turab")


# *args allows a function to accept any no of positional arguments
def add_numbers(*args):
    return sum(args)


print(add_numbers(10,20,80))

print(add_numbers(30,90,80,60))


# **kwargs allows a function to accept any numbers of keyword arguments ->return dictionary

def show_profile(**kwargs):
    print(kwargs)


show_profile(name="turab",age=23,gender="male")


def square(num):
    return num*num


ans = square(5)
print(ans)

def calculate(a,b):
    return  a+b,a-b,a*b


add,sub,mul = calculate(10,5)

print(add,sub,mul)



# nonlocal->keyword used in nested function to modify a variable from outer function

def outer():
    count = 0   
    print(count)
    def inner():
        nonlocal count
        count+=1
        print(count)

# lambda expression

square = lambda X:X*X

print(square(5))

add = lambda a,b:a+b
is_even = lambda a:a%2==0
to_upper = lambda text:text.upper()

print(add(8,8))
print(is_even(44))

print(to_upper("turab"))

