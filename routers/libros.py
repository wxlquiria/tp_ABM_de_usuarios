from fastapi import APIRouter, HTTPException, status

from models.libros import (
    CreateLibroResponse,
    DeleteLibroResponse,
    GetLibrosResponse,
    Libro,
    UpdateLibro,
    UpdateLibroResponse,
)

router = APIRouter()

books: list[Libro] = [
    Libro(id=1, titulo="La Divina Comedia", autor="Dante Alighieri", anio=1321, genero="Poesía épica, Narrativa poética"),
    Libro(id=2, titulo="Odisea", autor="Homero", anio=750, genero="Poema épico")
]

@router.get("/libro")
def get_books(genero: str | None = None) -> GetLibrosResponse:
    if genero is None:
        r = books
    else: 
        r = [u for u in books if genero.lower() in u.genero.lower()]

    return GetLibrosResponse(libros = r)
    

@router.delete("/libro/{id}")
def delete_libro(id: int) -> DeleteLibroResponse:
    for libro in books:
        if libro.id == id:
            books.remove(libro)
            return DeleteLibroResponse(message="Libro borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado"
    )


@router.post("/libro")
def create_user(libro: Libro) -> CreateLibroResponse:
    books.append(libro)
    return CreateLibroResponse(message="Libro registrado")


@router.patch("/libro/{id}")
def update_libro(id: int, datos: UpdateLibro) -> UpdateLibroResponse:
    for libro in books:
        if libro.id == id:
            cambios = datos.model_dump(exclude_unset=True)
            print(cambios)
            for campo, valor in cambios.items():
                setattr(libro, campo, valor)
            return UpdateLibroResponse(message="Libro actualizado")
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado"
    )



