from fastapi import APIRouter, HTTPException, status

from models.users import (
    CreateUserResponse,
    DeleteUserResponse,
    GetUsersResponse,
    UpdateUser,
    UpdateUserResponse,
    User,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]

@router.get("/user")
def get_users(is_active: bool | None = None) -> GetUsersResponse:
    if(is_active is None):
        r = usuarios
    else:
        r = [u for u in usuarios if u.is_active == is_active]
        
    return GetUsersResponse(users=r)
    


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="ususario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")


@router.patch("/user/{id}")
def update_user(id: int, datos: UpdateUser) -> UpdateUserResponse:
    for user in usuarios:
        if user.id == id:
            cambios = datos.model_dump(exclude_unset=True)
            print(cambios)
            for campo, valor in cambios.items():
                setattr(user, campo, valor)
            return UpdateUserResponse(message="usuario actualizado")
        

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )
