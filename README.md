## Aplikasi Manajemen Tiket Event — Tugas Individu WAD

Sistem manajemen dan pemesanan tiket event berbasis **FastAPI** (Backend) dan **Vue 3** (Frontend) yang dibangun untuk memenuhi kriteria Tugas Individu *Web Application Development*.

---

## 1. Prasyarat

Untuk menjalankan repositori ini di lingkungan lokal, pastikan perangkat kamu telah terpasang:
- **Python:** versi 3.10 atau lebih baru (untuk backend FastAPI dan eksekusi `verify.py`)
- **Node.js:** versi 18 atau lebih baru (termasuk `npm` untuk frontend Vue 3)
- **Git:** untuk *version control* dan manajemen branch workflow

---

## 2. Layanan

Aplikasi dibangun dengan arsitektur terpisah (*decoupled architecture*):

- **Backend Service (FastAPI):**
  - Mengelola logika bisnis tiket, validasi skema input/output Pydantic, dan penanganan HTTP response.
  - Berjalan di `http://127.0.0.1:8000`.
  - **Spesifikasi REST API Endpoint (`/api/tiket`):**
    - `POST /api/tiket` → Membuat tiket baru. Mengembalikan status **`201 Created`** beserta Header **`Location: /api/tiket/{id}`**.
    - `GET /api/tiket` → Mengambil daftar tiket. Mengembalikan status **`200 OK`** dan mendukung query parameter `skip`, `limit`, serta `search`.
    - `GET /api/tiket/{id}` → Mengambil detail tiket berdasarkan ID. Mengembalikan status **`404 Not Found`** jika ID tidak ditemukan.
    - **Validasi Input:** Mengembalikan status **`422 Unprocessable Entity`** jika payload input tidak valid. Skema Input (`TiketCreate`) dipisahkan dari Skema Output (`TiketResponse` yang memuat `id` buatan server).

- **Frontend Service (Vue 3 + Vite + TypeScript):**
  - Antarmuka pengguna (UI) berbasis komponen HTML semantik (`<header>`, `<main>`, `<section>`, `<h1>`) dan Composition API (`<script setup>`).
  - Berjalan di `http://localhost:5173`.

---

## 3. Cara Menjalankan

### A. Menjalankan Backend (FastAPI)
1. Buka terminal di root repo, lalu aktifkan *virtual environment*:
   ```bash
   source .venv/bin/activate  # Git Bash / Linux
   # atau .venv\Scripts\Activate.ps1 di Windows PowerShell

```

2. Pastikan dependensi backend terpasang:
```bash
pip install -r backend/requirements.txt

```


3. Jalankan server FastAPI:
```bash
uvicorn backend.app.main:app --reload

```


> Akses Dokumentasi Swagger UI di: `http://127.0.0.1:8000/docs`



### B. Menjalankan Frontend (Vue 3)

1. Buka terminal baru, lalu masuk ke direktori `frontend`:
```bash
cd frontend

```


2. Pasang dependensi Node.js:
```bash
npm install

```


3. Jalankan server pengembang:
```bash
npm run dev

```


> Akses antarmuka aplikasi di: `http://localhost:5173`



---

## 4. Cara Memverifikasi

### Pengujian Otomatis (Gate Check)

Untuk memverifikasi struktur proyek, dokumen, dan kriteria *Definition of Done* (DoD) Tugas Individu, jalankan skrip verifikasi dari root repositori:

```bash
python verify.py --individu

```

### Pengujian Manual (Swagger UI)

Buka `http://127.0.0.1:8000/docs` untuk menguji secara interaktif:

1. **`POST /api/tiket`**: Masukkan data tiket untuk menguji Response `201` dan Header `Location`.
2. **`POST /api/tiket`**: Masukkan payload invalid untuk menguji Response `422`.
3. **`GET /api/tiket/{id}`**: Panggil ID yang tidak terdaftar untuk menguji Response `404`.

---

## 5. Masalah yang Sering Muncul

* **`command not found: Remove-Item`:** Terjadi jika perintah PowerShell dijalankan di Git Bash. Gunakan perintah `rm` saat berada di Git Bash.
* **Port 8000 atau 5173 — *Address already in use*:** Hentikan proses server yang sedang berjalan sebelumnya menggunakan `Ctrl + C` sebelum me-running ulang.
* **`ModuleNotFoundError` untuk `fastapi` atau `uvicorn`:** Pastikan *virtual environment* (`.venv`) sudah diaktifkan sebelum menjalankan perintah `uvicorn`.
* **Pengujian `python verify.py --individu` Gagal:** Pastikan pengerjaan dilakukan di branch `feature/endpoint-individu` dan semua endpoint sudah terimplementasi sesuai spesifikasi.

```

```