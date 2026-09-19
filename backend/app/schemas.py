from pydantic import BaseModel, Field  # pyright: ignore[reportMissingImports]


class TiketBase(BaseModel):
    kode_tiket: str = Field(
        ...,
        pattern=r"^EVT-[A-Za-z0-9]{4}$",
        description="Pola kode tiket harus EVT-XXXX",
    )
    kuota: int = Field(..., gt=0, description="Kuota harus lebih dari 0")


class TiketCreate(TiketBase):
    pass


class TiketResponse(TiketBase):
    id: int

    class Config:
        from_attributes = True