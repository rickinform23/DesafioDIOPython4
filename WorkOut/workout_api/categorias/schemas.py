from typing import Annotated
from pydantic import UUID4, Field
from contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Scale", max_length=10)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua X, 002", max_length=60)]
    proprietario: Annotated[str, Field(description="Propriedade do centro de treinamento", example="Marcos", max_length=30)]
    
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da Categoria")]
    