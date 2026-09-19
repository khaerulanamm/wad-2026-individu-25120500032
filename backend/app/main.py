from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, Response, status

from .schemas import TiketCreate, TiketResponse

app = FastAPI(title="API Tiket")

@app.get("/")
def read_root():
    return {
        "message": "Selamat datang di API Tiket!",
        "docs": "Akses /docs untuk melihat dokumentasi API",
    }

db_tiket = []
id_counter = 1


# Endpoint /health (Wajib untuk lulus verify.py)
@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post(
    "/api/tiket",
    response_model=TiketResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_tiket(payload: TiketCreate, response: Response):
    global id_counter

    new_tiket = {"id": id_counter, **payload.model_dump()}
    db_tiket.append(new_tiket)

    response.headers["Location"] = f"/api/tiket/{id_counter}"

    id_counter += 1
    return new_tiket


@app.get("/api/tiket", response_model=List[TiketResponse])
def get_all_tiket(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    search: Optional[str] = Query(None),
):
    results = db_tiket

    if search:
        results = [
            t for t in results if search.lower() in t["kode_tiket"].lower()
        ]

    return results[skip : skip + limit]


@app.get("/api/tiket/{id}", response_model=TiketResponse)
def get_tiket_by_id(id: int):
    for tiket in db_tiket:
        if tiket["id"] == id:
            return tiket

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tiket tidak ditemukan"
    )