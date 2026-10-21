from pydantic import BaseModel,Field,field_validator
class User(BaseModel):
    id:int= Field(gt=0,description="it must be positive value greater than 0")
    name:str=Field(min_length=3,description="must be atleast greater than 3 characters")
    email:str
    age:int=Field(gt=18,lt=200,description="must be between 18 and 200 yrs")
    is_active:bool=True
    
    @field_validator("username")
    @classmethod
    def validate_username(cls,v:str)->str:
        if not v.isalnum():
            raise ValueError("username must be alphanumeric")
        return v.lower()
    
user = User(id=1,name="turab",email="demo@gmailcom",age=23)


# this one is valid pydantic infeeres it 
# user = User(id="1",name="turab",email="demo@gmailcom")
# wrong pydantic can process thhis
# user = User(id="one",name="turab",email="demo@gmailcom")



print(user)
print(user.name)
print(user.id)
print(user.email)


raw_data  ={
    "id":2,
    "name":"adam",
    "email":"demo1@gmail.com",
    "is_active":False,
    "age":24
    
}
user2 = User.model_validate(raw_data)

print(user2)