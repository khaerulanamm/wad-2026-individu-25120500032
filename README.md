## Aplikasi Manajemen Tiket Event

Sistem manajemen dan pemesanan tiket event full-stack berbasis **FastAPI** (Backend) dan **Vue 3** (Frontend).

## 1. Prasyarat
Untuk menjalankan aplikasi manajemen tiket ini di lingkungan lokal, pastikan perangkat kamu memiliki:
- **Python:** versi 3.10 atau lebih baru (untuk menjalankan backend FastAPI & skrip `verify.py`)
- **Node.js:** versi 18 atau lebih baru (termasuk `npm` untuk mengelola dependensi Vue 3)
- **Git:** untuk *version control* dan manajemen branch

## 2. Layanan
Aplikasi ini terdiri dari dua layanan utama yang saling terhubung (*decoupled architecture*):
- **Backend Service (FastAPI):**
  - Mengelola logika bisnis tiket, validasi skema data (`Pydantic`), dan rute REST API.
  - Berjalan di `http://127.0.0.1:8000`.
  - Endpoint kesehatan: `GET /health` (mengembalikan status server).
  - Endpoint tiket: `GET /api/v1/tiket`, `POST /api/v1/tiket` (manajemen data tiket event).
- **Frontend Service (Vue 3 + Vite + TypeScript):**
  - Antarmuka pengguna (UI) untuk menampilkan katalog event dan formulir pemesanan tiket.
  - Berjalan di `http://localhost:5173`.
  - Menggunakan komponen HTML semantik (`<header>`, `<main>`, `<section>`, `<h1>`) dan Composition API (`<script setup>`).

## 3. Cara menjalankan

### A. Menjalankan Backend (FastAPI)
1. Buka terminal di root repo, lalu aktifkan *virtual environment*:
   ```bash
   source .venv/bin/activate  # Linux / Git Bash

```

2. Pastikan pustaka backend terpasang:
```bash
pip install -r backend/requirements.txt

```


3. Jalankan server FastAPI:
```bash
uvicorn backend.app.main:app --reload

```


> Akses Dokumentasi Swagger UI di: `http://127.0.0.1:8000/docs`



### B. Menjalankan Frontend (Vue 3)

1. Buka terminal baru, lalu masuk ke direktori frontend:
```bash
cd frontend

```


2. Pasang pustaka Node.js:
```bash
npm install

```


3. Jalankan server pengembang Vue:
```bash
npm run dev

```


> Akses aplikasi di browser melalui: `http://localhost:5173`



## 4. Cara memverifikasi

Untuk memverifikasi bahwa seluruh struktur proyek, file konfig, dan kriteria *Definition of Done* (DoD) Sesi 2 sudah terpenuhi:

1. Pastikan *virtual environment* aktif.
2. Jalankan skrip verifikasi otomatis di root repositori:
```bash
python verify.py --sesi 2

```



## 5. Masalah yang sering muncul

* **Error `command not found: Remove-Item`:** Terjadi jika perintah PowerShell dijalankan di Git Bash. Gunakan `rm` untuk menghapus file di Git Bash.
* **Port `8000` atau `5173` *Address already in use*:** Server FastAPI atau Vite sebelumnya masih berjalan di background. Hentikan proses dengan `Ctrl + C` atau tutup terminal sebelumnya.
* **ModuleNotFoundError (`fastapi` / `uvicorn` tidak ditemukan):** Terjadi karena *virtual environment* belum diaktifkan. Jalankan `source .venv/bin/activate` terlebih dahulu.
* **CORS Error saat Frontend memanggil Backend:** Pastikan backend FastAPI sudah dikonfigurasi middleware CORS agar mengizinkan request dari `http://localhost:5173`.

```

```