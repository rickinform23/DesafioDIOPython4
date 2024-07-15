from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema 


class CentroTreinamentoIN(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT King", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua X, 002", max_length=60)]
    proprietario: Annotated[str, Field(description="Propriedade do centro de treinamento", example="Marcos", max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
     nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT King", max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIN):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]