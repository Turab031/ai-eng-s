# allow to mention expected type of variable an return variables
# since dynamically type ->error nhi deta

def greet(name:str)->str:
    return f"hello,{name}"


message = greet("turab")
print(message)


name:str = "turab"
age:int = 23
height:float = 6.0

def add(a:int,b:int)->int:
    return a+b

ans  = add(10,30)
print(ans)

from typing import Optional,Union,TypedDict,Any

numbers:list[int] = [1,2,3,4,5]
names:list[str] =["turab","najaf"]

# generics
student:dict[str,int]={
    "math":90,
    "science":85
}
# def print_Score(scores:dict[str,int])->None:
# optional->used when a value can either be a specific type or none

def find_user(user_id:int)->Optional[str]:
    if user_id==1:
        return "turab"
    return None

def find_user(user_id:int)->str|None:
    if user_id==1:
        return "turab"
    return None


# union->when return type value can be two type

def format_id(user_id:str|int)->str:
    return f"user-{user_id}"


# typedict->define expected structure of dictionary

class Student(TypedDict):
    name:str
    age:int
    course:str


student:Student={
    "name":"turab",
    "course":"ai-engineering",
    "age":23
}

print(student)