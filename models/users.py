from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True 

class GetUsersResponse(BaseModel):
    users: list[User]

class CreateUserResponse(BaseModel):
    message : str

class DeleteUserResponse(BaseModel):
    message: str

class UpdateUser(BaseModel):
    name: str | None = None
    is_active: bool | None = None


class UpdateUserResponse(BaseModel):
    message: str


