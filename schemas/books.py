from pydantic import BaseModel, ConfigDict, Field


class SBookBase(BaseModel):

    title: str = Field(description='Название книги')
    author: str = Field(description='Автор книги')
    year: int = Field(description='Год издания')
    pages: int = Field(description='Количество страниц', gt=10)
    is_read: bool | None = Field(description='Прочитана ли книга',
                                 default=False)


class SBookAdd(SBookBase):
    pass


class SBook(SBookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
