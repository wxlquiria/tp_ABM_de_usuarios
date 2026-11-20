from pydantic import BaseModel


class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    genero: str

class GetLibrosResponse(BaseModel):
    libros : list[Libro]

class CreateLibroResponse(BaseModel):
    message : str

class DeleteLibroResponse(BaseModel):
    message: str

class UpdateLibro(BaseModel):
    titulo: str | None = None
    autor: str | None = None
    anio: int
    genero: str


class UpdateLibroResponse(BaseModel):
    message: str

    